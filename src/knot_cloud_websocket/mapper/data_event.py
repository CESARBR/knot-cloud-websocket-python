'''
:mod:`knot_cloud_websocket.mapper.data_event` provides mapping for DataEventMessage.
'''

from ..message import DataEventMessage


def to_dictionary(message):
    '''
    Maps message to dictionary
    '''

    data = {
        'from': message.id,
        'payload': {
            'sensorId': message.sensorId,
            'value': message.value
        }
    }
    return {'type': 'data', 'data': data}


def from_dictionary(dictionary):
    '''
    Maps dictionary to message
    '''

    return DataEventMessage(dictionary['data']['from'],
                            dictionary['data']['payload']['sensorId'],
                            dictionary['data']['payload']['value'])
