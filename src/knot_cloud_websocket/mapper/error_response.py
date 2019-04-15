'''
:mod:`knot_cloud_websocket.mapper.error_response` provides mapping for :class:`ErrorResponseMessage`.
'''

from ..message import ErrorResponseMessage


def to_dictionary(message):
    '''
    Maps message to dictionary
    '''

    data = {'code': message.code, 'message': message.message}
    return {'type': 'error', 'data': data}


def from_dictionary(dictionary):
    '''
    Maps dictionary to message
    '''

    return ErrorResponseMessage(dictionary['data']['code'],
                                dictionary['data']['message'])
