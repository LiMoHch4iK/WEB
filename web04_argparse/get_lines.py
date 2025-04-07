import argparse


def count_lines(file_name):
    try:
        with open(file_name) as f:
            return len(f.readlines())
    except Exception:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    print(count_lines(args.file))