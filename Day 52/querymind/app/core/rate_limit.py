import time
from collections import defaultdict, deque

from fastapi import HTTPException, Request

MAX_REQUESTS = 15
WINDOW_SECONDS = 60

_request_log: dict[str, deque] = defaultdict(deque)


def _get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def enforce_rate_limit(request: Request) -> None:
    """Simple in-memory sliding-window rate limiter, per client IP.
    Suitable for a single-instance free-tier deployment (no shared store needed)."""
    client_ip = _get_client_ip(request)
    now = time.monotonic()
    log = _request_log[client_ip]

    while log and now - log[0] > WINDOW_SECONDS:
        log.popleft()

    if len(log) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please wait a moment before trying again.",
        )

    log.append(now)
