import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1.json))
    file2 = json.load(open(file_path2))
    diff = []

    diff = generate_diff(file_path1, file_path2)
    print(diff)
