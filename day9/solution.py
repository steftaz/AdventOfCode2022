sample = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


def solution1(inp):
    head = (0, 0)
    tail = (0, 0)
    visited = []
    mapping_location = {'D': (0, -1), 'L': (-1, 0), 'U': (0, 1), 'R': (1, 0)}

    for x in inp.split('\n')[:-1]:
        direction, amount = x.split()
        for _ in range(int(amount)):
            mp = mapping_location[direction]
            head = (head[0] + mp[0], head[1] + mp[1])
            match abs(diffx := head[0] - tail[0]) + abs(diffy := head[1] - tail[1]):
                case 2:
                    tail = (tail[0] + int(diffx / 2), tail[1] + int(diffy / 2))
                case 3:
                    if abs(diffx) == 2:
                        tail = (head[0] - int(diffx / 2), head[1])
                    elif abs(diffy) == 2:
                        tail = (head[0], head[1] - int(diffy / 2))
            visited.append(tail)
    return len(set(visited))


def solution2(inp):
    head = (0, 0)
    tails = [(0, 0) for _ in range(9)]
    visited = []
    mapping_location = {'D': (0, -1), 'L': (-1, 0), 'U': (0, 1), 'R': (1, 0)}
    for x in inp.split('\n')[:-1]:
        direction, amount = x.split()
        for _ in range(int(amount)):
            mp = mapping_location[direction]
            head = (head[0] + mp[0], head[1] + mp[1])
            temphead = head
            for i in range(len(tails)):
                tail = tails[i]
                new_tail = (head[0] - int((head[0] - tail[0]) / 2), head[1] - int((head[1] - tail[1]) / 2))
                head = new_tail
                tails[i] = new_tail
                if i == 8:
                    visited.append(new_tail)
            head = temphead
    return len(set(visited))


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
    # print(tail_position((1, -2), (0, 0)))
