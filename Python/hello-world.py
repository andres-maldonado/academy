import time


REFERENCE = {
    'D': ((1, 2, 3, 4), (1, 5), (1, 5), (1, 5), (1, 2, 3, 4)),
    'E': ((1, 2, 3, 4, 5), (1,), (1, 2, 3, 4), (1,), (1, 2, 3, 4, 5)),
    'H': ((1, 5), (1, 5), (1, 2, 3, 4, 5), (1, 5), (1, 5)),
    'L': ((1,), (1,), (1,), (1,), (1, 2, 3, 4, 5)),
    'O': ((1, 2, 3, 4, 5), (1, 5), (1, 5), (1, 5), (1, 2, 3, 4, 5)),
    'R': ((1, 2, 3, 4), (1, 5), (1, 2, 3, 4), (1, 5), (1, 6)),
    'W': ((0, 6), (0, 6), (0, 3, 6), (0, 3, 6), (1, 2, 4, 5))
}


def paint(word):
    # Canvas 5x7
    for letter in word:
        if letter == ' ':
            print('\n')
            continue
        _base = REFERENCE[letter.upper()]
        for lane in _base:
            _lane_to_print = ''
            for i in range(0, 7):
                _lane_to_print += '#' if i in lane else ' '
            print(_lane_to_print)
            time.sleep(0.1)
        print('\n')

paint('hello world')