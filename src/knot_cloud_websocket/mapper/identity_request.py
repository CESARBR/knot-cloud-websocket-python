'''
:mod:`knot_cloud_websocket.mapper.identity_request` provides mapping for :class:`IdentityRequestMessage`.
'''

from ..message import IdentityRequestMessage


def to_dictionary(message):
    '''
    Maps message to dictionary
    '''

    data = {'id': message.id, 'token': message.token}
    return {'type': message.type, 'data': data}


def from_dictionary(dictionary):
    '''
    Maps dictionary to message
    '''

    return IdentityRequestMessage(dictionary['data']['id'],
                                  dictionary['data']['token'])
