'''
:mod:`knot_cloud_websocket.client` provides the KNoT Cloud API client.
'''

import json

from .exception import UnknownMessageError
from .mapper import error_response, identity_request, ready_response
from .message import IdentityRequestMessage


class Client:
    '''
    KNoT Cloud API client
    '''

    def __init__(self, socket):
        self.__socket = socket
        self.__send_mappers = {'identity': identity_request}
        self.__recv_mappers = {
            'error': error_response,
            'ready': ready_response
        }

    async def identity(self, credential_id, credential_token):
        '''
        Identifies with the server.
        '''
        message = IdentityRequestMessage(credential_id, credential_token)
        await self.__send_message(message)

    async def receive(self):
        '''
        Receives a message from the server.

        Calling this method concurrently will raise :class:`RuntimeError`
        '''
        data = await self.__socket.recv()
        return self.__deserialize(data)

    async def __send_message(self, message):
        frame = self.__serialize(message)
        await self.__socket.send(frame)

    def __serialize(self, message):
        return json.dumps(
            self.__send_mappers[message.type].to_dictionary(message))

    def __deserialize(self, frame):
        dictionary = json.loads(frame)
        frame_type = dictionary['type']
        return self.__get_recv_mapper(frame_type).from_dictionary(dictionary)

    def __get_recv_mapper(self, frame_type):
        if not frame_type in self.__recv_mappers:
            raise UnknownMessageError(frame_type)
        return self.__recv_mappers[frame_type]
