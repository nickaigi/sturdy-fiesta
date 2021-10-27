def letter_combinations(self, digits: str) -> List[str]:
    data = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z'],
    }
    if len(digits) < 1:
        return []
    combo = [data[d] for d in digits]
    print(combo)
    return []


if __name__ == '__main__':
    print(letter_combinations('23')
