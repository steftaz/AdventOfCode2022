sample = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


def solution1(inp):
    for i in range(len(inp)):
        # Create a window with size 4
        window = inp[i:i+4]
        # Check if every value in the window is unique
        if len(window) == len(set(window)):
            return i + 4


def solution2(inp):
    for i in range(len(inp)):
        # Create a window with size 14
        window = inp[i:i+14]
        # Check if every value in the window is unique
        if len(window) == len(set(window)):
            return i + 14


def test1():
    inp = read_data('data/input.txt')
    print(f'solution for part one : {solution1(inp)}')


def test2():
    inp = read_data('data/input.txt')
    print(f'solution for part two : {solution2(inp)}')


def read_data(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    test1()
    test2()


