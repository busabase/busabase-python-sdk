"""A real user story against a REAL Busabase server, through the public SDK surface.

Skipped unless BUSABASE_TEST_BASE_URL is set. It creates a throwaway Base, a
record and a Doc, so it refuses to run against anything but a local server
unless BUSABASE_TEST_ALLOW_REMOTE=1 — never point it at a real workspace.

    npx busabase server --port 15419 --data ~/.cache/busabase-python-sdk-it
    BUSABASE_TEST_BASE_URL=http://127.0.0.1:15419 uv run pytest -m integration -s

A local self-hosted server is open, so no key is needed; set
BUSABASE_TEST_API_KEY / BUSABASE_TEST_SPACE_ID for a server that wants one.
"""

from __future__ import annotations

import os
import time
from urllib.parse import urlparse

import pytest

from busabase import Busabase, BusabaseError
from busabase.generated.models import (
    Base,
    ChangeRequest,
    CreatedEmbedLink,
    CreateNodeOperation,
    DocNodeDetail,
    EmbedFramePolicyOrigins,
    EmbedLinksCreateBody,
    FolderNodeDetail,
    MaterializedBase,
    MaterializedDoc,
    MaterializedRecord,
    NodesCreateChangeRequestBody,
    PendingChangeRequest,
    Record,
    RecordFilter,
    RecordSort,
    RecordValueAnyOf,
    RecordValueComparison,
)

BASE_URL = os.environ.get("BUSABASE_TEST_BASE_URL", "")

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(not BASE_URL, reason="set BUSABASE_TEST_BASE_URL to run against a real server"),
]


@pytest.fixture(scope="module")
def bb() -> Busabase:
    host = urlparse(BASE_URL).hostname
    if host not in ("localhost", "127.0.0.1", "::1") and os.environ.get("BUSABASE_TEST_ALLOW_REMOTE") != "1":
        pytest.skip(f"refusing to create test data on {host}; set BUSABASE_TEST_ALLOW_REMOTE=1 to override")
    return Busabase(
        api_key=os.environ.get("BUSABASE_TEST_API_KEY") or None,
        base_url=BASE_URL,
        space=os.environ.get("BUSABASE_TEST_SPACE_ID") or None,
    )


def record_fields(record: Record | MaterializedRecord) -> dict[str, object]:
    """A record's current field values live on its head commit."""
    return record.head_commit.payload.to_dict()


def test_base_record_doc_search_story(bb: Busabase) -> None:
    stamp = str(int(time.time()))
    slug = f"py-sdk-it-{stamp}"

    # 1. Look around: what Bases exist?
    before = bb.bases.list()
    assert all(isinstance(base, Base) for base in before)
    assert slug not in [base.slug for base in before]

    # 2. Create a Base with fields. With write access it merges in the same
    #    call; without it, it is a Change Request waiting for review.
    created = bb.bases.create(
        body={
            "slug": slug,
            "name": f"Python SDK IT {stamp}",
            "description": "Created by the busabase Python SDK integration test",
            "message": "Create a scratch Base for the Python SDK integration test",
            "fields": [
                {"slug": "company", "name": "Company", "type": "text"},
                {"slug": "score", "name": "Score", "type": "number"},
            ],
        }
    )
    if isinstance(created, PendingChangeRequest):
        pytest.skip(f"Base creation is waiting for review ({created.id}); the story needs write access")
    assert isinstance(created, MaterializedBase)
    assert [field.slug for field in created.fields] == ["company", "score"]
    assert slug in [base.slug for base in bb.bases.list()]

    # 3. Add a record — a Change Request. Never pass autoMerge: the server
    #    decides. Same handling as the Dify plugin: merged -> the record comes
    #    back; in review -> report the pending Change Request and stop there.
    company = f"Acme {stamp}"
    written = bb.bases.create_change_request(
        base_id=created.id,
        body={"fields": {"company": company, "score": 7}, "message": f"Add {company} — Python SDK test"},
    )
    if isinstance(written, PendingChangeRequest):
        assert written.status == "in_review"
        assert bb.change_requests.get(change_request_id=written.id).id == written.id
        pytest.skip(f"record write is in review as {written.id}; nothing merged to read back")
    assert isinstance(written, MaterializedRecord)
    record_id = written.id
    assert record_fields(written) == {"company": company, "score": 7}

    # 4. Read it back: in the list, and by id.
    page = bb.records.list(base_id=created.id)
    assert [record.id for record in page.records] == [record_id]
    fetched = bb.records.get(record_id=record_id)
    assert isinstance(fetched, Record)
    assert record_fields(fetched) == {"company": company, "score": 7}

    # 5. Write a Doc and read its body back.
    doc_slug = f"py-sdk-notes-{stamp}"
    doc_body = f"# Call notes\n\n{company} wants a demo next week. Marker zebra-{stamp}.\n"
    doc = bb.docs.create(
        body={"slug": doc_slug, "name": f"Call notes {stamp}", "body": doc_body, "message": "Add call notes"}
    )
    assert isinstance(doc, MaterializedDoc), doc
    detail = bb.nodes.get(doc.node.id)
    assert isinstance(detail, DocNodeDetail)
    assert detail.node.slug == doc_slug
    assert detail.body == doc_body

    # 6. Find both again. grep scans records and Docs with one pattern;
    #    search is the ranked full-text index.
    found = bb.grep(body={"pattern": f"zebra-{stamp}|{company}", "sources": ["records", "nodes"]}).to_dict()
    assert {m.get("recordId") for m in found["matches"] if m["source"] == "records"} == {record_id}, found
    assert {m.get("nodeId") for m in found["matches"] if m["source"] == "nodes"} == {doc.node.id}, found
    hits = bb.search(query=f"zebra-{stamp}")
    assert doc.node.id in [hit.id for hit in hits.results]

    # 7. Share the Doc as an embed link. This operation used to be dropped by
    #    the generator; omitting framePolicy must still get the server default.
    link = bb.embed_links.create(body={"type": "node", "typeId": doc.node.id})
    assert isinstance(link, CreatedEmbedLink)
    assert link.frame_policy.to_dict() == {"mode": "anywhere", "allowedOrigins": []}

    # 8. The same, but restricted to one site — built from the named request
    #    models (0.2.0) instead of a dict. The server normalizes the origin.
    pinned = bb.embed_links.create(
        body=EmbedLinksCreateBody(
            type_="node",
            type_id=doc.node.id,
            frame_policy=EmbedFramePolicyOrigins(mode="origins", allowed_origins=["https://example.com/"]),
        )
    )
    assert isinstance(pinned, CreatedEmbedLink)
    assert pinned.frame_policy.to_dict() == {"mode": "origins", "allowedOrigins": ["https://example.com"]}

    # 9. Restructure the tree with a typed node operation: a folder for the notes.
    folder_slug = f"py-sdk-folder-{stamp}"
    proposed = bb.nodes.create_change_request(
        body=NodesCreateChangeRequestBody(
            operations=[
                CreateNodeOperation(kind="create", node_type="folder", slug=folder_slug, name=f"Calls {stamp}")
            ],
            message="Add a folder for call notes",
        )
    )
    assert isinstance(proposed, ChangeRequest)
    if proposed.status == "in_review":
        pytest.skip(f"the folder is in review as {proposed.id}; nothing merged to read back")
    assert proposed.status == "merged", proposed.status
    folder = bb.nodes.get(folder_slug, type_="folder")
    assert isinstance(folder, FolderNodeDetail)
    assert folder.node.name == f"Calls {stamp}"

    # 10. A missing record is an error you can branch on, not a silent None.
    with pytest.raises(BusabaseError) as caught:
        bb.records.get(record_id=f"rec_missing_{stamp}")
    assert caught.value.status == 404
    assert caught.value.code == "NOT_FOUND"


def test_record_query_parameters(bb: Busabase) -> None:
    """filters / sort / valueFilters reach the server — they are object query parameters (bracket notation)."""
    stamp = str(int(time.time()))
    created = bb.bases.create(
        body={
            "slug": f"py-sdk-qp-{stamp}",
            "name": f"Python SDK query params {stamp}",
            "message": "Create a scratch Base for the Python SDK query-parameter test",
            "fields": [
                {"slug": "company", "name": "Company", "type": "text"},
                {"slug": "n", "name": "N", "type": "number"},
            ],
        }
    )
    if isinstance(created, PendingChangeRequest):
        pytest.skip(f"Base creation is waiting for review ({created.id}); the test needs write access")
    assert isinstance(created, MaterializedBase)
    # Created in this order, so neither creation order matches a sort by `n`.
    for company, n in [("Acme", 3), ("Beta", 1), ("Acme", 2)]:
        written = bb.bases.create_change_request(
            base_id=created.id, body={"fields": {"company": company, "n": n}, "message": f"Add {company} {n}"}
        )
        if isinstance(written, PendingChangeRequest):
            pytest.skip(f"record write is in review as {written.id}")

    def ns(page: object) -> list[float]:
        return [record_fields(record)["n"] for record in page.records]  # type: ignore[attr-defined]

    by_n = RecordSort(field_slug="n", field_type="number", direction="asc")

    # A view filter: only the Acme rows. View filters are pushed down to the server only
    # with a `fieldType` (text/number/checkbox); without one the page is a documented superset.
    acme = bb.records.list(
        base_id=created.id,
        filters=[RecordFilter(field_slug="company", field_type="text", operator="equals", value="Acme")],
    )
    assert sorted(record_fields(record)["company"] for record in acme.records) == ["Acme", "Acme"]

    # Sort ascending and descending — a dropped sort comes back in creation order instead.
    assert ns(bb.records.list(base_id=created.id, sort=by_n)) == [1, 2, 3]
    descending = RecordSort(field_slug="n", field_type="number", direction="desc")
    assert ns(bb.records.list(base_id=created.id, sort=descending)) == [3, 2, 1]

    # Exact value filters: a comparison, and an OR group.
    at_least_two = [RecordValueComparison(field_slug="n", operator="gte", value=2)]
    assert ns(bb.records.list(base_id=created.id, value_filters=at_least_two, sort=by_n)) == [2, 3]
    one_or_three = RecordValueAnyOf(
        any_=[
            RecordValueComparison(field_slug="n", operator="eq", value=1),
            RecordValueComparison(field_slug="n", operator="eq", value=3),
        ]
    )
    assert ns(bb.records.list(base_id=created.id, value_filters=[one_or_three], sort=by_n)) == [1, 3]
    assert bb.records.count(base_id=created.id, value_filters=at_least_two).total == 2
