def solution1(inp):
    pass


def solution2(inp):
    pass


def test1():
    inp = read_data('data/1')
    print(f'solution for part one : {solution1(inp)}')


def test2():
    inp = read_data('data/2')
    print(f'solution for part two : {solution2(inp)}')


def read_data(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    test1()
    test2()


