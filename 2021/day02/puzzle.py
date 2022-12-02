from dataclasses import dataclass

input = open("input.txt", "r").read().splitlines()


@dataclass
class Pos:
    horizontal: int
    depth: int

    def add(self, add):
        self.horizontal += add.horizontal
        self.depth += add.depth

    def __str__(self):
        return str(self.horizontal * self.depth)


def part_one():
    position = Pos(0, 0)
    for command in input:
        direction, length = command.split(" ")
        if direction == "forward":
            position.add(Pos(int(length), 0))
        elif direction == "up":
            position.add(Pos(0, -int(length)))
        else:
            position.add(Pos(0, int(length)))

    print(position)


@dataclass
class PosWithAim(Pos):
    aim: int

    def add(self, add):
        self.horizontal += add.horizontal
        self.depth += add.depth
        self.aim += add.aim


def part_two():
    position = PosWithAim(0, 0, 0)
    for command in input:
        direction, arg = command.split(" ")
        length = int(arg)
        if direction == "forward":
            position.add(PosWithAim(length, position.aim * length, 0))
        elif direction == "up":
            position.add(PosWithAim(0, 0, -length))
        else:
            position.add(PosWithAim(0, 0, length))

    print(position)


part_one()
part_two()
