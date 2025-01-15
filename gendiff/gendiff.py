import os

from gendiff.parser import get_data
from gendiff.build_diff import build_diff
from gendiff.formatting import format_diff


def get_continuation(file_path):
    return os.path.splitext(file_path)[1][1:]


def generate_diff(file_1, file_2, format="stylish"):
    dict_1 = get_data(file_1)
    dict_2 = get_data(file_2)
    diff = build_diff(dict_1, dict_2)
    return format_diff(diff, format)
