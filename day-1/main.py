"""
Author  :benni347:
"""


def read_file():
    filename: str = "input"
    content = []
    with open(filename) as f:
        for line in f:
            content.append(int(line.strip("\n")))
        f.close()

    return content


def check_if_increased_part_1(file_content: list):
    differences = 0
    for i in range(len(file_content)):
        if i == 0:
            i += 1
        else:
            if file_content[i] > file_content[i - 1]:
                differences += 1
            i += 1
    return differences


def three_sum_part_2(file_content: list):
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
    # content = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    differences_part_1 = check_if_increased_part_1(content)
    differences_part_2 = three_sum_part_2(content)
    print(differences_part_2)
