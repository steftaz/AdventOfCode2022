def solution1(inp):
    inp = inp.split('\n')
    res = []
    subres = []
    for x in inp:
        if x:
            subres.append(int(x))
        else:
            res.append(sum(subres))
            subres = []
    return max(res)


def solution2(inp):
    inp = inp.split('\n')
    res = []
    subres = []
    for x in inp:
        if x:
            subres.append(int(x))
        else:
            res.append(sum(subres))
            subres = []
    res.sort(reverse=True)
    return sum(res[:3])


def test1():
    inp = read_data('data/input1.txt')
    print(f'solution for part one : {solution1(inp)}')


def test2():
    inp = read_data('data/input1.txt')
    print(f'solution for part two : {solution2(inp)}')


def read_data(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    test1()
    test2()


