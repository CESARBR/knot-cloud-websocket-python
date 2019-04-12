'''
:mod:`knot_cloud_websocket.client` provides the KNoT Cloud API client.
'''

import json

from .mapper import identity_request
from .message import IdentityRequestMessage


class Client:  # pylint: disable=too-few-public-methods
    '''
    KNoT Cloud API client
    '''

    def __init__(self, socket):
        self.__socket = socket
        self.__send_mappers = {'identity': identity_request}

    async def identity(self, credential_id, credential_token):
        '''
        Identifies with the server.
        '''
        message = IdentityRequestMessage(credential_id, credential_token)
        await self.__send_message(message)

    async def __send_message(self, message):
        frame = self.__serialize(message)
        await self.__socket.send(frame)

    def __serialize(self, message):
        return json.dumps(
            self.__send_mappers[message.type].to_dictionary(message))
