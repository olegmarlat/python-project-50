import json


def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
    diff = []
    for key in sorted(dict1.keys() | dict2.keys()):
        if key not in dict2:
            diff.append(f' - {key}: {str(dict1[key])}')
        elif key not in dict1:
            diff.append(f' + {key}: {str(dict2[key])}')
