from typing import Annotated
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketDisconnect,
    WebSocketException,
    status,
)

app = FastAPI()


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Annotated[str | None, Cookie()] = None,
    token: Annotated[str | None, Query()] = None,
):
    if session is None and token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return session or token


@app.websocket("/messaging")
async def websocket_endpoint(
    websocket: WebSocket,
    cookie_or_token: Annotated[str, Depends(get_cookie_or_token)],
    q: int | None = None,
):
    await websocket.accept()
    print("cookie", cookie_or_token)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received data {data}")
            print(f"Cookie/query_token {cookie_or_token}")
            if q is not None:
                await websocket.send_text(f"Query parameter is:", {q})
            await websocket.send_text(data)
    except WebSocketDisconnect:
        print(f"client disconnected")
