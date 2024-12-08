from json import dumps


def convert_to_json(diff):
    return dumps(diff, indent=4)
