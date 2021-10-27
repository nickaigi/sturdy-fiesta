from itertools import product


def letter_combinations(digits: str) -> list:
    """
    The Cartesian product of two lists is the set containing all ordered pairs
    (x, y) such that x belongs to the first list and y belongs to the second.

    E.g the Cartesian product of [1, 2] and ['a'] is [(1, 'a'), (2, 'a')]
    """
    data = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    temp = []

    if len(digits) < 1:
        return []

    for d in digits:
        temp.append(data[d])
    # Call itertools.product(*args) with multiple lists as *args to find their
    # Cartesian product as an itertools.product object
    # we use the unpacking operator, and starmap()
    return [*map(''.join, product(*temp))]


if __name__ == '__main__':
    print(letter_combinations('23'))
