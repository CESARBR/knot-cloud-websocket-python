from knot_cloud_websocket.mapper.error_response import *
from knot_cloud_websocket.message import ErrorResponseMessage


def test_error_response_mapper_to_dictionary_should_convert_to_dictionary():
    message = ErrorResponseMessage(403, "Forbidden")
    expected = {'type': 'error', 'data': {'code': 403, 'message': 'Forbidden'}}

    actual = to_dictionary(message)

    assert actual == expected, "Should convert to dictionary"


def test_error_response_mapper_from_dictionary_should_convert_to_message():
    dictionary = {
        'type': 'error',
        'data': {
            'code': 403,
            'message': 'Forbidden'
        }
    }
    expected = ErrorResponseMessage(403, "Forbidden")

    actual = from_dictionary(dictionary)

    assert actual == expected, "Should convert to message"
