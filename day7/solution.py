from typing import Self, List

sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Directory:
    def __init__(self, name: str, parent: Self | None, level: int):
        self.name = name
        self.parent = parent
        self.level = level
        self.children: List[Self | File] = []

    def add_child(self, child):
        self.children.append(child)

    def size(self) -> int:
        res = 0
        for child in self.children:
            res += child.size()
        return res
        # return sum(child.size() for child in self.children)

    def special_size(self) -> list:
        dir_size = self.size()
        res = [dir_size]
        for child in self.children:
            if type(child) == type(self):
                res += child.special_size()
        return res

    def get_child(self, name: str) -> Self | False:
        for child in self.children:
            if child.name == name:
                return child
        return False

    def __str__(self) -> str:
        return f"{'  ' * self.level}- {self.name} dir\n" + "".join([str(child) for child in self.children])


class File:
    def __init__(self, name: str, size: int, parent: Directory):
        self.name = name
        self.level = parent.level + 1
        self.file_size = size

    def size(self) -> int:
        return self.file_size

    def special_size(self):
        return []

    def __str__(self) -> str:
        return '  ' * self.level + f'- {self.name} size={self.file_size}\n'


def solution1(inp):
    root = parse(inp)
    return sum(filter(lambda x: x < 100000, root.special_size()))


def solution2(inp):
    root = parse(inp)
    dir_sizes = root.special_size()
    available = 70000000 - 30000000 - max(dir_sizes)
    return min(filter(lambda x: x > -available, dir_sizes))


def parse(inp):
    root = Directory('/', parent=None, level=0)
    current = root
    for line in inp.split('\n')[1:-1]:
        if line[0] == '$':
            command = line[2:4]
            if command == 'cd':
                location = line[5:]
                if location == '..':
                    current = current.parent
                elif location == '/':
                    current = root
                else:
                    name = location
                    if child := current.get_child(name):
                        current = child
                    else:
                        child = Directory(location, current, current.level + 1)
                        current.add_child(child)
                        current = child
            elif command == 'ls':
                continue
        else:
            size, name = line.split()
            if size == 'dir':
                continue
            file = File(name, int(size), current)
            current.add_child(file)
    print(root)
    return root


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


