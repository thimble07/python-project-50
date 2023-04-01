import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('file_path', metavar='first_file', type=str)
parser.add_argument('file_path', metavar='second_file', type=str)

args = parser.parse_args()
print(args.accumulate(args.integers))
