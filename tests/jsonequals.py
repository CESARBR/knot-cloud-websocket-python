import jsondiff


def are_json_equal(json1, json2):
    return not any(jsondiff.diff(json1, json2, load=True))
