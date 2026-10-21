from __future__ import annotations

from typing import Any

import httpx


class BusabaseError(Exception):
    """A Busabase API call failed (HTTP status >= 400).

    Built from the `{ error, code, data }` body every `/api/v1` endpoint returns
    on failure, so `code` is the server's semantic outcome (`NOT_FOUND`,
    `FORBIDDEN`, `BAD_REQUEST`, `CONFLICT`, …) rather than just the status.

    Attributes:
        status: HTTP status code.
        code: The server's error code, or `HTTP_<status>` when the body had none.
        message: The server's message; for a 400, field-level validation issues
            are appended (`fields.0.slug: Required`).
        data: The envelope's `data` (e.g. `{"issues": [...]}`), if any.
        response: The raw `httpx.Response`.
    """

    def __init__(
        self,
        message: str,
        *,
        status: int,
        code: str,
        data: Any = None,
        response: httpx.Response | None = None,
    ) -> None:
        super().__init__(f"{code} ({status}): {message}")
        self.message = message
        self.status = status
        self.code = code
        self.data = data
        self.response = response

    @classmethod
    def from_response(cls, response: httpx.Response) -> BusabaseError:
        """Decode an error response. The body must already be read."""
        status = response.status_code
        try:
            body = response.json()
        except ValueError:
            body = None
        if not isinstance(body, dict) or not isinstance(body.get("error"), str):
            text = response.text.strip()
            return cls(text or response.reason_phrase, status=status, code=f"HTTP_{status}", response=response)

        message: str = body["error"]
        data = body.get("data")
        issues = data.get("issues") if isinstance(data, dict) else None
        if isinstance(issues, list) and issues:
            details = []
            for issue in issues:
                if not isinstance(issue, dict):
                    details.append(str(issue))
                    continue
                path = issue.get("path")
                where = ".".join(str(step) for step in path) if isinstance(path, list) and path else ""
                details.append(f"{where}: {issue.get('message')}" if where else str(issue.get("message")))
            message = f"{message} — {'; '.join(details)}"
        code = body.get("code")
        return cls(
            message,
            status=status,
            code=code if isinstance(code, str) else f"HTTP_{status}",
            data=data,
            response=response,
        )
