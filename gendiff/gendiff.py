import json


file_1.json:{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}

file_path2.json:{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}

def generate_diff(file_path11, file_path2):
    file1 = json.load(open(file_path11.json))
    file2 = json.load(open(file_path2))
    diff = []

    diff = generate_diff(file_path1, file_path2)
    print(diff)
