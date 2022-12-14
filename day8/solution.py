sample = """30373
25512
65332
33549
35390
"""


def solution1(inp):
    inp = [[int(x) for x in y] for y in inp.split('\n')[:-1]]
    transpose = [[inp[y][x] for y in range(len(inp))] for x in range(len(inp[0]))]
    res = 2*len(inp) + 2*len(inp[0]) - 4
    for y in range(1, len(inp) - 1):
        for x in range(1, len(inp[y]) - 1):
            up = max(transpose[x][0:y])
            right = max(inp[y][x+1:len(inp[x])])
            down = max(transpose[x][y+1:len(transpose[y])])
            left = max(inp[y][0:x])
            house = inp[y][x]
            if house > up or house > right or house > down or house > left:
                res += 1
    return res


def solution2(inp):
    inp = [[int(x) for x in y] for y in inp.split('\n')[:-1]]
    transpose = [[inp[y][x] for y in range(len(inp))] for x in range(len(inp[0]))]
    scores = []
    for y in range(1, len(inp) - 1):
        for x in range(1, len(inp[y]) - 1):
            up = score(inp[y][x], reversed(transpose[x][0:y]))
            right = score(inp[y][x], inp[y][x+1:len(inp[x])])
            down = score(inp[y][x], transpose[x][y+1:len(transpose[y])])
            left = score(inp[y][x], reversed(inp[y][0:x]))
            scores.append(up*right*down*left)
    return max(scores)


def score(height, direction):
    res = 0
    for x in direction:
        res += 1
        if x >= height:
            return res
    return res


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


