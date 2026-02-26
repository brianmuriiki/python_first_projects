import argparse
import os

def count_lines(file):
    with open(file, "r") as f:
        return len(f.readlines())

def count_words(file):
    with open(file, "r") as f:
        text = f.read()
        return len(text.split())

def file_size(file):
    return os.path.getsize(file)

def main():
    parser = argparse.ArgumentParser(description="Simple File Analyzer CLI")

    parser.add_argument("", help="")
    parser.add_argument("--lines", action="store_true", help="Count lines")
    parser.add_argument("--words", action="store_true", help="Count words")
    parser.add_argument("--size", action="store_true", help="Show file size")

    args = parser.parse_args()

    if args.lines:
        print("Lines:", count_lines(args.file))

    if args.words:
        print("Words:", count_words(args.file))

    if args.size:
        print("Size:", file_size(args.file), "bytes")

if __name__ == "__main__":
    main()

