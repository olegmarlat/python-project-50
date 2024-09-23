#!/usr/bin/env python3

import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="Set format of output")
    args = parser.parse_args()
    print(args)

diff = generate_diff(file_path1, file_path2)
print(diff)


if __name__ == "__main__":
    main()
