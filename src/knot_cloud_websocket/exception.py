'''
:mod:`knot_cloud_websocket.exception` provides exceptions raised by other modules.
'''


class UnknownMessageError(Exception):
    '''
    Raised when an unknown message is received.
    '''
