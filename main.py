from stats import get_num_words, get_num_chars, sorted_dict
from sys import argv, exit


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_content = get_book_text(argv[1])
    num_words = get_num_words(book_content)
    num_chars = get_num_chars(book_content)
    sort = sorted_dict(num_chars)
    print(f"Found {num_words} total words")
    for c in sort:
        ch = c["char"]
        num = c["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
        else:
            continue


def get_book_text(path):
    filepath = path
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
