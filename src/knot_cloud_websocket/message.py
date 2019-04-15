'''
:mod:`knot_cloud_websocket.message` provides types for messages exchanged with KNoT Cloud
'''

from dataclasses import dataclass


@dataclass
class IdentityRequestMessage:
    '''
    Represents 'identity' message.
    '''

    id: str
    token: str
    type: str = 'identity'


@dataclass
class ReadyResponseMessage:
    '''
    Represents 'ready' message.
    '''

    type: str = 'ready'


@dataclass
class ErrorResponseMessage:
    '''
    Represents 'error' message.
    '''

    code: int
    message: str
    type: str = 'error'


@dataclass
class DataEventMessage:
    '''
    Represents 'data' event
    '''

    id: str
    sensorId: int
    value: type(None)
