'''
:mod:`knot_cloud_websocket.factory` provides a factory for KNoT Cloud API client.
'''

from contextlib import asynccontextmanager

import websockets

from .client import Client
from .exception import AuthenticationError
from .message import ReadyResponseMessage
from .uri import build_uri

FIVE_SECONDS = 5
FIFTEEN_SECONDS = 15
FIVE_MINUTES = 5 * 60


def _is_websocket(protocol):
    return protocol in ('ws', 'wss')


def _is_port(port):
    return 1 <= port <= 65535


def _validate_arguments(protocol, hostname, port, credential_id,
                        credential_token):
    if not _is_websocket(protocol):
        raise ValueError("protocol should be 'ws' or 'wss'")
    if hostname is None:
        raise ValueError("hostname is required")
    if not _is_port(port):
        raise ValueError("port must be a valid port number")
    if credential_id is None:
        raise ValueError("credential_id is required")
    if credential_token is None:
        raise ValueError("credential_token is required")


@asynccontextmanager
async def _create_socket(uri, use_ssl):
    ssl_context = use_ssl or None  # True means "use the default SSL context"
    async with websockets.connect(uri,
                                  ssl=ssl_context,
                                  ping_interval=FIFTEEN_SECONDS,
                                  ping_timeout=FIVE_MINUTES,
                                  close_timeout=FIVE_SECONDS) as socket:
        yield socket


def _create_client(socket):
    return Client(socket)


async def _identify(client, credential_id, credential_token):
    await client.identity(credential_id, credential_token)
    response = await client.receive()
    if not isinstance(response, ReadyResponseMessage):
        raise AuthenticationError(response)


@asynccontextmanager
async def create_connection(*,
                            protocol='wss',
                            hostname=None,
                            port=443,
                            pathname=None,
                            credential_id=None,
                            credential_token=None):
    '''
    Creates a WebSocket connection to a KNoT Cloud instance.

    The KNoT Cloud instance URI is `protocol`://`hostname`:`port`/`pathname`. After connecting,
    it will authenticate the connection using `credential_id`/`credential_token`.
    '''

    _validate_arguments(protocol, hostname, port, credential_id,
                        credential_token)

    uri = build_uri(protocol, hostname, port, pathname)

    async with _create_socket(uri, protocol == 'wss') as socket:
        client = _create_client(socket)
        await _identify(client, credential_id, credential_token)
        yield client
