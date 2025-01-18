import json
# from json import dumps


# def convert_to_json(diff):
#   return dumps(diff, indent=4)


def convert_to_json(diff):
    result = json.dumps(diff, indent=2)
    return result
