import argparse

from gendiff import generate_diff


def parser_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="Set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, style=args.format)
    print(diff)

# return args.first_file, args.second_file, args.format
