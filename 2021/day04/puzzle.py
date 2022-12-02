import re


class Board:
    def __init__(self, board):
        self.rows = [
            [int(x) for x in re.split("\\s+", row.strip())]
            for row in board.split("\n")
            if row != ""
        ]
        self.columns = list(map(list, zip(*self.rows)))

    def get_score(self, drawn):
        score = sum([
            x
            for row in self.rows
            for x in row
            if x not in drawn
        ])
        return score

    def check_line(self, drawn, line):
        for i, board_num in enumerate(line):
            if board_num not in drawn:
                return False
            elif i == len(line) - 1:
                return True
        return False

    def has_bingo(self, drawn):
        for row in self.rows:
            if self.check_line(drawn, row):
                return True
        for col in self.columns:
            if self.check_line(drawn, col):
                return True
        return False


[input_numbers, input_boards] = open("input.txt", "r").read().split("\n", 1)
numbers = [int(x) for x in input_numbers.split(",")]
boards = [
    Board(board)
    for board in re.split("^\n", input_boards, flags=re.MULTILINE)
    if board != ""
]
num_boards = len(boards)

drawn = numbers[:4]
for num in numbers[4:]:
    drawn.append(num)
    for i, board in enumerate(boards):
        if (board.has_bingo(drawn)):
            score = board.get_score(drawn)
            if len(boards) == num_boards:
                print(f"Part one: {score * int(num)}")
            elif len(boards) == 1:
                print(f"Part two: {score * int(num)}")
                quit()
            boards.remove(board)
