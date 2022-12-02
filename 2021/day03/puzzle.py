input = open("input.txt", "r").read().splitlines()


def part_one():
    gamma_rate = ""
    epsilon_rate = ""
    for bits in map(list, zip(*map(list, input))):
        if sum(map(int, bits)) >= len(bits) / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    result = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"Part one: {result}")


def get_common(bins, pos):
    bits = [bits[pos] for bits in bins]
    return "1" if sum(map(int, bits)) >= len(bits) / 2 else "0"


def part_two():
    report = list(input)

    oxygen_rating = report.copy()
    scrubber_rating = report.copy()

    for pos in range(len(report[0])):
        if len(oxygen_rating) > 1:
            oxygen_rating = [
                bin for bin in oxygen_rating if bin[pos] == get_common(oxygen_rating, pos)
            ]
        if len(scrubber_rating) > 1:
            scrubber_rating = [
                bin for bin in scrubber_rating if bin[pos] != get_common(scrubber_rating, pos)
            ]

    result = int(oxygen_rating[0], 2) * int(scrubber_rating[0], 2)
    print(f"Part two: {result}")


part_one()
part_two()
