def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        out = f.read()
    return out


def get_num_words(book_str: str) -> int:
    return sum([i for i in book_str.replace('  ', ' ').replace('\n', ' ').split(' ') if len(i) > 0])


def main():
    num_words = get_num_words(get_book_text('books/frankenstein.txt'))
    print(f"{num_words} words found in the document")


if __name__ == '__main__':
    main()
