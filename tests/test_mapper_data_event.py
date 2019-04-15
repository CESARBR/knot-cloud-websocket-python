from knot_cloud_websocket.mapper.data_event import *
from knot_cloud_websocket.message import DataEventMessage


def test_data_event_mapper_to_dictionary_should_convert_to_dictionary():
    message = DataEventMessage('abcdef', 1, 10)
    expected = {
        'type': 'data',
        'data': {
            'id': 'abcdef',
            'sensorId': 1,
            'value': 10
        }
    }

    actual = to_dictionary(message)

    assert actual == expected, "Should convert to dictionary"


def test_data_event_mapper_from_dictionary_should_convert_to_message():
    dictionary = {
        'type': 'data',
        'data': {
            'id': 'abcdef',
            'sensorId': 1,
            'value': 10
        }
    }
    expected = DataEventMessage('abcdef', 1, 10)

    actual = from_dictionary(dictionary)

    assert actual == expected, "Should convert to message"
