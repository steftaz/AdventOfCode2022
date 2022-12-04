sample = "vJrwpWtwJgWrhcsFMMfFFhFp\n" \
         "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n" \
         "PmmdzqPrVvPwwTWBwg\n" \
         "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n" \
         "ttgJtRGJQctTZtZT\n" \
         "CrZsJsPPZsGzwwsLwLmpwMDw\n"


def solution1(inp):
    # Create list where each index equals the priority for its value ('a' is on index 1 and has priority 1)
    priority = [''] + [chr(x) for x in range(97, 123)] + [chr(x) for x in range(65, 91)]
    # Split the input into a list with each value being one rucksack
    inp = inp.split('\n')[:-1]
    score = 0
    for x in inp:
        # Split each rucksack into its two compartments
        front, back = x[:len(x)//2], x[len(x)//2:]
        # Find the common value between the two compartments
        common = set(front).intersection(set(back)).pop()
        # Add all priorities
        score += priority.index(common)
    return score


def solution2(inp):
    # Create list where each index equals the priority for its value ('a' is on index 1 and has priority 1)
    priority = [''] + [chr(x) for x in range(97, 123)] + [chr(x) for x in range(65, 91)]
    # Split input into usable groups of 3 rucksacks each
    inp = inp.split('\n')[:-1]
    groups = [inp[i:i+3] for i in range(0, len(inp), 3)]
    # Find the intersecting value for each group and add all their priorities
    return sum(priority.index(set(x[0]).intersection(set(x[1]), set(x[2])).pop()) for x in groups)


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


