"""
Author  :benni347:
"""


def read_file():
    """
    This reads the file.
    :return: a list of all ints in the given file.
    """
    filename: str = "input"
    local_content = []
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            local_content.append(int(line.strip("\n")))
        f.close()

    return local_content


def check_if_increased_part_1(file_content: list):
    """
    To solve part 1 of the problem.
    :param file_content: a list with the numbers of input.
    :return: the amount of differences.
    """
    differences = 0
    for i, _ in enumerate(file_content):
        if i == 0:
            i += 1
        else:
            if file_content[i] > file_content[i - 1]:
                differences += 1
            i += 1
    return differences


def three_sum_part_2(file_content: list):
    """
    To solve part 2 of the problem.
    :param file_content: a list with the numbers of input.
    :return: the amount of differences.
        """
    previous_sum = file_content[0] + file_content[1] + file_content[2]
    differences = 0
    for i in range(1, len(file_content) - 2, 1):
        new_sum = file_content[i] + file_content[i + 1] + file_content[i + 2]
        if new_sum > previous_sum:
            differences += 1
        previous_sum = new_sum
    return differences


if __name__ == "__main__":
    content = read_file()
    DIFFERENCES_PART_1 = check_if_increased_part_1(content)
    DIFFERENCES_PART_2 = three_sum_part_2(content)
    print(f"Part 1: {DIFFERENCES_PART_1}")
    print(f"Part 2: {DIFFERENCES_PART_2}")
