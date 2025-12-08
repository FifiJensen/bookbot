import sys
from stats import get_num_words, get_num_chars, get_sort_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_dict = get_sort_dict(num_chars)
    for item in sorted_dict:
        print(f"{item["char"]}: {item["num"]}")
    print_report(book_path, num_words, sorted_dict)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
