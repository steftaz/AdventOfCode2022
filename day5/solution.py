sample = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def solution1(inp):
    # Get the input into a usable format
    stacks, moves = parse(inp)
    # Move consist of (times, source, destination)
    for move in moves:
        # Move the amount specified in the move instruction
        for i in range(int(move[0])):
            # Remove the highest crate in the stack
            crate = stacks[move[1]].pop()
            # Put the crate on the destination stack
            stacks[move[2]].append(crate)
    # Create a string with all top crates
    return ''.join([x[-1] for x in stacks.values()])


def solution2(inp):
    # Get the input into a usable format
    stacks, moves = parse(inp)
    # Move consist of (times, source, destination)
    for move in moves:
        # Take the amount of specified crates (move[0]) and put them on the destination stack (move[2])
        stacks[move[2]].extend(stacks[move[1]][-int(move[0]):])
        # Remove the moved crates from the destination stack (move[1])
        stacks[move[1]] = stacks[move[1]][:-int(move[0])]
    # Create a string with all the top crates
    return ''.join([x[-1] for x in stacks.values()])


# TODO: Improve readability and add comments
def parse(inp):
    start = []
    for x in inp.split('\n'):
        if x == '':
            break
        start.append([x[i] for i in range(1, len(x), 4)])
    stacks = {}
    for x in start[-1]:
        stack = []
        for i in range(len(start)-2, -1, -1):
            crate = start[i][int(x)-1]
            if crate != ' ':
                stack.append(crate)
            else:
                break
        stacks[x] = stack
    inp = inp.split('\n')[len(start) + 1:-1]
    moves = []
    for x in inp:
        x = x.split()
        moves.append((x[1], x[3], x[5]))
    return stacks, moves


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


