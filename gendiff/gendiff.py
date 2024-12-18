from gendiff.parser import get_data
from gendiff.build_diff import build_diff
from gendiff.formatting import format_diff


def generate_diff(file2_1, file2_2, format="stylish"):
    dict_1 = get_data(file2_1)
    dict_2 = get_data(file2_2)
    diff = build_diff(dict_1, dict_2)
    return format_diff(diff, format)
