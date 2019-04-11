import pytest

from knot_cloud_websocket import create_connection


@pytest.mark.asyncio
async def test_should_raise_when_hostname_is_not_passed():
    with pytest.raises(ValueError):
        async with create_connection(protocol='wss',
                                     port=443,
                                     pathname='/ws',
                                     credential_id='anyid',
                                     credential_token='anytoken'):
            pass


@pytest.mark.asyncio
async def test_should_raise_when_id_is_not_passed():
    with pytest.raises(ValueError):
        async with create_connection(protocol='wss',
                                     hostname='ws.knot.cloud',
                                     port=443,
                                     pathname='/ws',
                                     credential_token='anytoken'):
            pass


@pytest.mark.asyncio
async def test_should_raise_when_token_is_not_passed():
    with pytest.raises(ValueError):
        async with create_connection(protocol='wss',
                                     hostname='ws.knot.cloud',
                                     port=443,
                                     pathname='/ws',
                                     credential_id='anyid'):
            pass
