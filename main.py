from stats import get_num_words, get_sorted_num_chars

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        out = f.read()
    return out


def print_report(book_path: str, book_str: str):
    data = {
        "word_count": get_num_words(book_str),
        "char_count": [
            f"{i['char']}: {i['num']}"
            for i in get_sorted_num_chars(book_str)
        ]
    }
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {data['word_count']} total words")
    print("--------- Character Count -------")
    for i in data['char_count']:
        print(i)
    print("============= END ===============")


def main():
    book_path = 'books/frankenstein.txt'
    print_report(book_path, get_book_text(book_path))


if __name__ == '__main__':
    main()
