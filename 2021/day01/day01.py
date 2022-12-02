input_arr = open("day01.input.txt", "r").read().splitlines()
measurements = list(map(int, input_arr))


def count_increases(nums):
    increases = 0
    for i, v in enumerate(nums[1:]):
        if v > nums[i]:
            increases += 1
    return increases


def add_3(nums):
    acc = []
    for i in range(len(nums[2:])):
        acc.append(sum(nums[i:i + 3]))
    return acc


print('Part 1 answer is: {}'.format(count_increases(measurements)))
print('Part 2 answer is: {}'.format(count_increases(add_3(measurements))))
