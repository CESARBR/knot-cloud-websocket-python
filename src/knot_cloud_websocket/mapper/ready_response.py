'''
:mod:`knot_cloud_websocket.mapper.ready_response` provides mapping for :class:`ReadyResponseMessage`.
'''

from ..message import ReadyResponseMessage


def to_dictionary(message):
    '''
    Maps message to dictionary
    '''
    del message  # unused
    return {'type': 'ready'}


def from_dictionary(dictionary):
    '''
    Maps dictionary to message
    '''
    del dictionary  # unused
    return ReadyResponseMessage()
