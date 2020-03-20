__author__ = "ハリネズミ"


def is_isbn_or_key(word):
    # isbn isbn13 13個0~9の数値
    # isbn10 10個0~9の数値, 一部" - "も含む
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    shot_word = word.replace('-', '')
    if "-" in word and len(shot_word) == 10 and shot_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
