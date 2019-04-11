'''
:mod:`knot_cloud_websocket.uri` provides URI utilities.
'''

from urllib.parse import urlunparse


def build_uri(protocol, hostname, port, pathname):
    '''
    Builds an URI string from parts of it.
    '''

    netloc = "{hostname}:{port}".format(hostname=hostname, port=port)
    return urlunparse((protocol, netloc, pathname or '', None, None, None))
