from gendiff.gendiff import generate_diff


file_result = open('./tests/fixtures/result_test1.txt')
result_test_json = file_result.read()


def test_generate_diff():
    assert generate_diff(
        './tests/fixtures/file1.json', './tests/fixtures/file2.json') == result_test_json

result_test_yml = yml.load(open('./tests/fixtures/result_test_yml.txt'))

def test_generate_diff():
    assert generate_diff(
        file_path1: './tests/fixtures/file1.yml', file_path2: './tests/fixtures/file2.yml') == result_test_yml
