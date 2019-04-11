from knot_cloud_websocket import uri


def test_build_uri_should_add_double_slash_to_protocol_when_missing():
    expected = 'ws://ws.knot.cloud:443/ws'

    actual = uri.build_uri('ws', 'ws.knot.cloud', 443, '/ws')

    assert actual == expected, "Should add double slash to protocol when missing"


def test_build_uri_should_add_colon_between_hostname_and_port():
    expected = 'ws://ws.knot.cloud:443/ws'

    actual = uri.build_uri('ws', 'ws.knot.cloud', 443, '/ws')

    assert actual == expected, "Should add colon between hostname and port"


def test_build_uri_should_add_slash_before_pathname_when_missing():
    expected = 'ws://ws.knot.cloud:443/ws'

    actual = uri.build_uri('ws', 'ws.knot.cloud', 443, 'ws')

    assert actual == expected, "Should add slash before pathname when missing"


def test_build_uri_should_not_add_slash_before_pathname_when_present():
    expected = 'ws://ws.knot.cloud:443/ws'

    actual = uri.build_uri('ws', 'ws.knot.cloud', 443, '/ws')

    assert actual == expected, "Should not add slash before pathname when present"
