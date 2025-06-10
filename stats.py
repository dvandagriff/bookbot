def get_num_words(book_str: str) -> int:
    book_str = (
        book_str
        .replace('  ', ' ')
        .replace('\n', ' ')
    )
    return len([
        i for i in book_str.split(' ') if len(i) > 0])


def get_num_chars(book_str: str) -> dict:
    out = {}
    for i in book_str:
        _i = i.lower()
        if _i not in out:
            out[_i] = 1
        else:
            out[_i] += 1
    return out


def get_sorted_num_chars(book_str: str) -> list:
    out = [
        {'char': k, 'num': v}
        for k,v in get_num_chars(book_str).items()
        if k.isalpha()
    ]
    out.sort(reverse=True, key=lambda a: a['num'])
    return out
