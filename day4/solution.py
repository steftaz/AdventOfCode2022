import re

sample = "2-4,6-8\n" \
         "2-3,4-5\n" \
         "5-7,7-9\n" \
         "2-8,3-7\n" \
         "6-6,4-6\n" \
         "2-6,4-8\n"


# TODO: Cleanup and commenting still necessary
def solution1(inp):
    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    values = re.findall(pattern, inp)
    count = 0
    for x in values:
        x = [int(value) for value in x]
        if (x[0] <= x[2] and x[1] >= x[3]) or \
                (x[0] >= x[2] and x[1] <= x[3]):
            count += 1
    return count


def solution2(inp):
    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    values = re.findall(pattern, inp)
    count = 0
    for x in values:
        x = [int(value) for value in x]
        if (x[0] <= x[2] <= x[1]) or \
                (x[0] <= x[3] <= x[1]) or \
                (x[2] <= x[0] <= x[3]) or \
                (x[2] <= x[1] <= x[3]):
            count += 1
    return count


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
