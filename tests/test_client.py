import asyncio

import pytest

from jsonequals import are_json_equal
from knot_cloud_websocket.client import Client


@pytest.fixture
def socket(mocker):
    patcher = mocker.patch('websockets.client.WebSocketClientProtocol')
    _socket = patcher()
    send_result = asyncio.Future()
    send_result.set_result(None)
    _socket.send.return_value = send_result
    return _socket


@pytest.mark.asyncio
async def test_identity_should_call_send_on_socket(socket):
    client = Client(socket)

    await client.identity('myid', 'mytoken')

    assert socket.send.called, "Should call send on socket"


@pytest.mark.asyncio
async def test_identity_should_call_send_with_json_frame(socket):
    expected = '{ "type": "identity", "data":{ "id": "myid", "token": "mytoken" } }'
    client = Client(socket)

    await client.identity('myid', 'mytoken')

    actual = socket.send.call_args[0][0]
    assert are_json_equal(actual, expected), "Should call send with JSON frame"
