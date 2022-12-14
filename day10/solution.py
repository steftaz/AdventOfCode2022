sample = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

def solution1(inp):
    x = 1
    res = 0
    cycle = 0

    check = list(range(20, 221, 40))
    lines = inp.split('\n')[:-1]

    for line in lines:
        if line == 'noop':
            cycle, res = up_cycle(cycle, check, res, x)
        else:
            amount = int(line.split()[1])
            cycle, res = up_cycle(cycle, check, res, x)
            cycle, res = up_cycle(cycle, check, res, x)
            x += amount
    return res


def up_cycle(cycle, check, res, x):
    cycle += 1
    if cycle in check:
        res += x * cycle
    return cycle, res


def solution2(inp):
    x = 1
    res = "\n"
    cycle = 0

    check = list(range(40, 241, 40))
    lines = inp.split('\n')[:-1]

    for line in lines:
        if line == 'noop':
            cycle, res = up_cycle2(cycle, check, res, x)
        else:
            amount = int(line.split()[1])
            cycle, res = up_cycle2(cycle, check, res, x)
            cycle, res = up_cycle2(cycle, check, res, x)
            x += amount
    return res


def up_cycle2(cycle, check, res, x):
    if cycle in check:
        res += '\n'
    if x - 1 <= cycle % 40 <= x + 1:
        res += '#'
    else:
        res += '.'
    cycle += 1
    return cycle, res


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


