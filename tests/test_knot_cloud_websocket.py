import knot_cloud_websocket


def test_version_should_be_0_1_0():
    assert knot_cloud_websocket.__version__ == '0.1.0', "Version should be 0.1.0"


def test_should_export_create_connection():
    assert hasattr(knot_cloud_websocket,
                   'create_connection'), "Should export 'create_connection()'"
