from knot_cloud_websocket.mapper.identity_request import *
from knot_cloud_websocket.message import IdentityRequestMessage


def test_identity_request_mapper_to_dictionary_should_convert_to_dictionary():
    message = IdentityRequestMessage('myid', 'mytoken')
    expected = {'type': 'identity', 'data': {'id': 'myid', 'token': 'mytoken'}}

    actual = to_dictionary(message)

    assert actual == expected, "Should convert to dictionary"


def test_identity_request_mapper_from_dictionary_should_convert_to_message():
    dictionary = {
        'type': 'identity',
        'data': {
            'id': 'myid',
            'token': 'mytoken'
        }
    }
    expected = IdentityRequestMessage('myid', 'mytoken')

    actual = from_dictionary(dictionary)

    assert actual == expected, "Should convert to message"
