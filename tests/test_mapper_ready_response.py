from knot_cloud_websocket.mapper.ready_response import *
from knot_cloud_websocket.message import ReadyResponseMessage


def test_ready_response_mapper_to_dictionary_should_convert_to_dictionary():
    message = ReadyResponseMessage()
    expected = {'type': 'ready'}

    actual = to_dictionary(message)

    assert actual == expected, "Should convert to dictionary"


def test_ready_response_mapper_from_dictionary_should_convert_to_message():
    dictionary = {'type': 'ready'}
    expected = ReadyResponseMessage()

    actual = from_dictionary(dictionary)

    assert actual == expected, "Should convert to message"
