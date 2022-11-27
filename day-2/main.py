"""
URL     :https://adventofcode.com/2021/day/2:
Author  :benni347:
"""


def read_file():
    """
    This reads the file.
    :return: a list of all ints in the given file.
    """
    filename: str = "input"
    local_content = []
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            local_content.append(str(line.strip("\n")))
        file.close()

    return local_content


def dive_part_1(file_content: list):
    """
    To solve part 1 of the problem.
    :param file_content: a list with the directions of input.
    :return: the amount of differences.
    """
    horizontal = 0
    vertical = 0
    for i, direction in enumerate(file_content):
        if direction[:7] == "forward":
            horizontal += int(direction[8:])
        elif direction[:2] == "up":
            vertical -= int(direction[3:])
        elif direction[:4] == "down":
            vertical += int(direction[5:])
        i += 1
    return horizontal * vertical


def dive_part_2(file_content: list):
    """
    To solve part 2 of the problem.
    :param file_content: a list with the directions of input.
    :return: the amount of differences.
    """
    horizontal = 0
    vertical = 0
    aim = 0
    for i, direction in enumerate(file_content):
        if direction[:7] == "forward":
            change = int(direction[8:])
            horizontal += change
            vertical += aim * change
        elif direction[:2] == "up":
            change = int(direction[3:])
            aim -= change
        elif direction[:4] == "down":
            change = int(direction[5:])
            aim += change
        i += 1
    return vertical * horizontal


if __name__ == "__main__":
    content = read_file()
    PART_1 = dive_part_1(content)
    PART_2 = dive_part_2(content)
    print(f"Part 1: {PART_1}")
    print(f"Part 2: {PART_2}")
