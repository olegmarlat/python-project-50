import pytest
import os
from pathlib import Path
from gendiff import generate_diff

BASE_DIR = Path(__file__).parent


@pytest.mark.parametrize("file_1, file_2, expected, format", [
    (
        "file1.json",
        "file2.json",
        "stylish.txt",
        "stylish"
    ),
    (
        "file1.yml",
        "file2.yml",
        "stylish.txt",
        "stylish"),
    (
        "file3.json",
        "file4.json",
        "plain.txt",
        "plain"
    ),
    (
        "file5.yml",
        "file6.yml",
        "plain.txt",
        "plain"
    ),
    (
        "file3.json",
        "file4.json",
        "json.txt",
        "json"
    ),
    (
        "file5.yml",
        "file6.yml",
        "json.txt",
        "json"
    ),
])
def test_gendiff(file_1, file_2, expected, format):
    file_1_path = os.path.join(BASE_DIR, "fixtures", file_1)
    file_2_path = os.path.join(BASE_DIR, "fixtures", file_2)
    expected_path = os.path.join(BASE_DIR, "fixtures", expected)

    result = generate_diff(file_1_path, file_2_path, format)
    with open(expected_path, "r") as expected_file:
        assert result == expected_file.read()
