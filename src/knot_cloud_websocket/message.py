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
