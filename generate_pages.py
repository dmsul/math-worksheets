from typing import Tuple
from numpy.random import randint

CELL = " \\problem{{{}}}{{{}}}{{{}}} "


def make_page(operator: str, min_len: int, max_len: int, path: str):
    """
    Args
    ----

    `operator` (str): Addition? Subtraction? Maybe '\\times' or '\\div'. This
        string will be inserted into a math environment in Latex, so don't use
        '$' anywhere.
    `min_len` (int): Minimum digits in the numbers used.
    `max_len` (int): Maximum digits in the numbers used.
    `path` (str): Path to save file
    """
    page = ''
    j = 1
    for i in range(28):
        a, b = get_num_pair(min_len, max_len)
        val = CELL.format(a, operator, b)
        if j == 4:
            page += val + '\\\\ \\addlinespace[.5in]\n'
            j = 1
        else:
            page += val + '\\quad\\quad\\quad&'
            j += 1

    with open(path, 'w') as f:
        f.write(page)


def get_num_pair(min_len: int, max_len: int) -> Tuple[str, ...]:
    a, b = get_num(min_len, max_len), get_num(min_len, max_len)
    if b > a:
        a, b = b, a

    strs = str(a), str(b)
    need_len = max(map(len, strs))
    return tuple(map(lambda x: _fill_tilde(x, need_len), strs))

def _fill_tilde(a: str, need_len: int) -> str:
    """Use phantom spaces to right justify numbers when needed"""
    return a.rjust(need_len, '~')


def get_num(min_len: int, max_len: int) -> int:
    this_len = num_len(min_len, max_len)
    return randint(10 ** (this_len - 1), 10 ** this_len)


def num_len(min_len: int, max_len: int) -> int:
    return randint(min_len, max_len + 1)


if __name__ == "__main__":
    prefix = 'tmp'
    # `x` is page number.
    for x in range(1, 3):
        make_page('+', 2, 3, f'{prefix}{x}.tex')
    for x in range(3, 5):
        make_page('-', 1, 2, f'{prefix}{x}.tex')
    for x in range(5, 7):
        make_page('\\times', 1, 2, f'{prefix}{x}.tex')
    for x in range(7, 9):
        make_page('\\div', 1, 2, f'{prefix}{x}.tex')
