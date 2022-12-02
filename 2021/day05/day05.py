import re

input = open("day05.input.txt").read().splitlines()

number_regex = re.compile("(\\d+)")


def get_points(x1, y1, x2, y2):
    if x1 == x2:
        return [[x1, y] for y in range(min(y1, y2), max(y1, y2) + 1)]
    if y1 == y2:
        return [[x, y1] for x in range(min(x1, x2), max(x1, x2) + 1)]
    return []


points = [
    point
    for line in input
    for points in get_points(*map(int, number_regex.findall(line)))
    for point in points
]

print(sorted(points))
