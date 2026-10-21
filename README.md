# busabase — the Busabase Python SDK

The official Python client for the [Busabase](https://busabase.com) REST API: Bases and records,
Docs, files, skills, search, and the Change Requests every write goes through. One client works
against Busabase Cloud and any self-hosted Busabase server.

- **Typed models for every endpoint**, generated from the Busabase OpenAPI document with
  [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
- **A small hand-written layer** on top: configuration from the same environment variables as the
  Busabase CLI, `bb.<group>.<operation>(...)` calls, and a typed `BusabaseError` for every failed
  request instead of a silent `None`.
- Sync and async. Python 3.11+.

## Install

```bash
pip install busabase
# or
uv add busabase
```

## Quick start

```python
from busabase import Busabase

bb = Busabase(api_key="bb_...")  # or set BUSABASE_API_KEY
for base in bb.bases.list():
    print(base.slug, base.name)
record = bb.records.get(record_id="rec_...")
print(record.head_commit.payload.to_dict())  # the record's field values
```

## Busabase Cloud or self-hosted

| | Busabase Cloud | Self-hosted server |
| --- | --- | --- |
| `base_url` / `BUSABASE_BASE_URL` | `https://busabase.com` (the default) | your server, e.g. `http://localhost:15419` |
| `api_key` / `BUSABASE_API_KEY` | required — create one in the dashboard | not needed for a local server |
| `space` / `BUSABASE_SPACE_ID` | needed when your key belongs to more than one space | usually not needed |

```python
bb = Busabase()  # everything from the environment
bb = Busabase(base_url="http://localhost:15419")  # a local `busabase server`
bb = Busabase(api_key="bb_...", space="spc_...")  # a specific Cloud space
```

`base_url` may include `/api/v1` or not. These are the same variables the Busabase CLI and the
TypeScript SDK (`busabase-sdk`) read.

**Cloud-only endpoints.** The SDK covers the full public API. A few groups exist only on Busabase
Cloud and return 404 from a self-hosted server: `system` (`health`, `meta`), `users.me`, and
`agent_tasks`.

## Writing: Change Requests

Every write in Busabase is a Change Request. When your key has write access it merges in the same
call and you get the materialized object back; otherwise it waits for a person to review it. Check
which one you got:

```python
from busabase.generated.models import MaterializedRecord, PendingChangeRequest

result = bb.bases.create_change_request(
    base_id="bas_...",
    body={"fields": {"company": "Acme", "score": 7}, "message": "Add Acme — inbound lead"},
)
if isinstance(result, MaterializedRecord):
    print("merged:", result.id)
elif isinstance(result, PendingChangeRequest):
    print("waiting for review:", result.id)
```

Don't pass `autoMerge` — let the server decide based on your permissions.

## Calling operations

Operations are grouped the way the API is (`bases`, `records`, `nodes`, `docs`, `file_trees`,
`change_requests`, `search`, `grep`, …), with snake_case names. `dir(bb)` and `dir(bb.records)`
list them.

```python
bb.bases.list()
bb.records.list(base_id="bas_...", limit=20)
bb.nodes.get("nod_...")  # path parameters can be positional
bb.docs.create(body={"slug": "notes", "name": "Notes", "body": "# Hi"})
bb.grep(body={"pattern": "acme", "sources": ["records", "nodes"]})
bb.nodes.share.list()  # nested groups
await bb.records.get.asyncio(record_id="rec_...")  # async
```

Each one calls the generated function of the same name in `busabase.generated.api` and returns its
parsed model (from `busabase.generated.models`). A request `body` can be a plain `dict` or the
generated model. For full static typing, call the generated module directly with `bb.client`:

```python
from busabase.generated.api.records import records_list

page = records_list.sync(client=bb.client, base_id="bas_...")
```

## Errors

Any HTTP status of 400 or above raises `BusabaseError` — from `bb.…` calls and from the generated
functions alike — carrying the server's error envelope:

```python
from busabase import BusabaseError

try:
    bb.records.get(record_id="rec_missing")
except BusabaseError as error:
    print(error.status, error.code, error.message)  # 404 NOT_FOUND Record not found: rec_missing
```

`code` is the server's semantic outcome (`NOT_FOUND`, `FORBIDDEN`, `BAD_REQUEST`, `CONFLICT`, …).
For a validation failure `message` spells out each field (`fields.0.slug: Invalid input: …`) and `data`
holds the raw `issues`.

## Configuration

```python
Busabase(
    api_key=None,  # BUSABASE_API_KEY
    base_url=None,  # BUSABASE_BASE_URL, then https://busabase.com
    space=None,  # BUSABASE_SPACE_ID
    timeout=30.0,  # seconds, or an httpx.Timeout
    headers=None,  # extra headers on every request
    httpx_args=None,  # passed to httpx.Client / httpx.AsyncClient (proxy, verify, transport…)
)
```

Use it as a context manager (`with Busabase() as bb:`) or call `bb.close()` to release connections.

## Changes in 0.2.0

Request models that used to have positional, generated names now have real ones, so you can build
a request from typed models instead of a `dict` (a `dict` still works everywhere). **If you import
any of the old names from `busabase.generated.models`, rename them** — the wire format and every
`bb.<group>.<operation>(...)` call are unchanged.

| 0.1.0 | 0.2.0 |
| --- | --- |
| `NodesCreateChangeRequestBodyOperationsItemType0` … `Type4` | `CreateNodeOperation`, `RenameNodeOperation`, `DeleteNodeOperation`, `RestoreNodeOperation`, `MoveNodeOperation` |
| `FileTreesCreateChangeRequestBodyOperationsItemType0` … `Type3` | `AssetFileOperation`, `TextFileOperation`, `DeleteFileOperation`, `FileTreeMetadataOperation` |
| `FileTreesCreateBodyFilesItemType0` / `Type1` | `AssetFileInput` / `TextFileInput` |
| `ViewsChangeRequestBodyType0` … `Type3` | `CreateViewOperation`, `UpdateViewOperation`, `DeleteViewOperation`, `RestoreViewOperation` |
| `NodesUpdateContentBodyContentType0` … `Type3` | `DocNodeContent`, `WhiteboardNodeContent`, `WorkflowNodeContent`, `HtmlNodeContent` |
| `EmbedLinksCreateBodyFramePolicyType0` … `Type2` | `EmbedFramePolicyAnywhere`, `EmbedFramePolicyOrigins`, `EmbedFramePolicyTopLevelOnly` |
| `WebhooksCreateBodyType0` … `Type2`, `WebhooksCreateBodyType0Config` | `HttpWebhookRuleInput`, `NotifyAgentWebhookRuleInput`, `RunFunctionWebhookRuleInput`, `WebhookHttpConfigInput` |
| `RecordsListFiltersItem` (and the `count` / `group_by` / `list_page` copies), `RecordsListSort` | `RecordFilter`, `RecordSort` |
| `RecordsListValueFiltersItemType0` / `Type1` (and copies) | `RecordValueComparison` / `RecordValueAnyOf` |
| `ViewConfigFiltersItem`, `ViewConfigSortsItem` | `ViewFilter`, `ViewSort` |
| `FieldOptionsChoicesItem`, `FieldOptionsHelp`, `BasesFieldChangeRequestBodyPatchOptions*` | `FieldChoice`, `FieldHelp`, the shared `FieldOptions*` models |
| `BaseFieldNameType1` (and copies) | `LocalizedFieldName` |
| `FormBindingsItem`, `FormPageTheme`, `FormsCreateBody*` / `FormsUpdateBody*` copies | `FormFieldBinding`, `FormTheme`, the shared `FormPage` / `FormShare` |
| `NodeAgentPromptsAgentPromptsType0Item` (and the update-body copy), `…LabelType1` / `…BodyType1` | `NodeAgentPrompt`, `LocalizedText` |
| `NodesResolveRouteStateResponse200Type0` … `Type2` | `ActiveNodeRouteState`, `ArchivedNodeRouteState`, `UnavailableNodeRouteState` |
| `FileTreesPreparePreviewResponse200Type0` … `Type2` | `BuiltinFilePreview`, `ReadyFilePreview`, `UnavailableFilePreview` |
| `ChangeRequestsReviewResponse200ResultsItemType0`, `ChangeRequestsMergeResponse200ResultsItemType0`, `…Type1` | `ChangeRequestReviewSuccess`, `ChangeRequestMergeSuccess`, `ChangeRequestBatchFailure` |
| `WorkflowDocumentNodesItemType0` … `Type7`, `…Position` | `TriggerWorkflowNode`, `WebhookWorkflowNode`, `FunctionWorkflowNode`, `ConditionWorkflowNode`, `WaitWorkflowNode`, `ApprovalWorkflowNode`, `ActionWorkflowNode`, `EndWorkflowNode`, `WorkflowNodePosition` |
| `AuthVerifyResponse200Space` / `…SpacesItem`, `MaterializedBaseReviewPolicy` | `AuthSpace`, `BaseReviewPolicy` |

```python
from busabase.generated.models import CreateNodeOperation, NodesCreateChangeRequestBody

bb.nodes.create_change_request(
    body=NodesCreateChangeRequestBody(
        operations=[CreateNodeOperation(kind="create", node_type="folder", slug="calls", name="Calls")],
        message="Add a folder for call notes",
    )
)
```

**Fixed: object and array query parameters.** `filters`, `value_filters` and `sort` on
`records.list` / `list_page` / `count` / `group_by` (plus `date_range`, `aggregates`, and
`status` on `change_requests.list` / `list_page`) are now sent the way the server reads them —
`filters[0][fieldSlug]=company&sort[direction]=desc`. In 0.1.0 a filter list was rejected with a
400 and `sort` was silently ignored (an unsorted page). They accept the generated models or plain
dicts, through `bb.…` and through `busabase.generated.api` alike:

```python
from busabase.generated.models import RecordFilter, RecordSort, RecordValueComparison

page = bb.records.list(
    base_id="bas_...",
    filters=[RecordFilter(field_slug="company", field_type="text", operator="equals", value="Acme")],
    value_filters=[RecordValueComparison(field_slug="score", operator="gte", value=40)],
    sort=RecordSort(field_slug="score", field_type="number", direction="desc"),
)
```

View `filters` are a best-effort superset unless they carry a `field_type`; `value_filters` are
always exact.

## Development

```bash
uv sync                                    # Python 3.11+, installs the pinned generator too
uv run pytest                              # unit tests + generated-code drift check
BUSABASE_TEST_BASE_URL=http://127.0.0.1:15419 uv run pytest -m integration   # against a local server
```

`src/busabase/generated/` is generated — never edit it by hand. It is produced from `openapi.json`
by `scripts/generate.py`, and `tests/test_generated.py` fails if the two disagree:

```bash
uv run python scripts/generate.py          # regenerate after openapi.json changes
uv run python scripts/generate.py --check  # what the test runs
```

## License

MIT
