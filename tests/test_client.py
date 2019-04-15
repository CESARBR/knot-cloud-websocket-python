import asyncio

import pytest
from websockets.client import WebSocketClientProtocol

from jsonequals import are_json_equal
from knot_cloud_websocket.client import Client
from knot_cloud_websocket.exception import UnknownMessageError
from knot_cloud_websocket.message import (ErrorResponseMessage,
                                          ReadyResponseMessage)


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


@pytest.mark.asyncio
async def test_receive_should_call_recv_on_socket(socket):
    result = '{ "type": "ready" }'
    recv = asyncio.Future()
    recv.set_result(result)
    socket.recv.return_value = recv
    client = Client(socket)

    await client.receive()

    assert socket.recv.called, "Should call recv on socket"


@pytest.mark.asyncio
async def test_receive_should_return_ready_response_message_when_ready_frame(
        socket):
    result = '{ "type": "ready" }'
    recv = asyncio.Future()
    recv.set_result(result)
    socket.recv.return_value = recv
    client = Client(socket)

    message = await client.receive()

    assert isinstance(
        message, ReadyResponseMessage), "Should return ReadyResponseMessage"


@pytest.mark.asyncio
async def test_receive_should_return_error_response_message_when_error_frame(
        socket):
    result = '{ "type": "error", "data": { "code": 403, "message": "Forbidden" } }'
    recv = asyncio.Future()
    recv.set_result(result)
    socket.recv.return_value = recv
    client = Client(socket)

    message = await client.receive()

    assert isinstance(
        message, ErrorResponseMessage), "Should return ErrorResponseMessage"


@pytest.mark.asyncio
async def test_receive_should_return_error_response_message_details_when_error_frame(
        socket):
    expected = ErrorResponseMessage(403, "Forbidden")
    result = '{ "type": "error", "data": { "code": 403, "message": "Forbidden" } }'
    recv = asyncio.Future()
    recv.set_result(result)
    socket.recv.return_value = recv
    client = Client(socket)

    actual = await client.receive()

    assert actual == expected, "Should return ErrorResponseMessage details"


@pytest.mark.asyncio
async def test_identity_raises_on_unknown_message(socket):
    result = '{ "type": "unknown" }'
    recv = asyncio.Future()
    recv.set_result(result)
    socket.recv.return_value = recv
    client = Client(socket)

    with pytest.raises(UnknownMessageError):
        message = await client.receive()
