"""
URL     :https://adventofcode.com/2021/day/3:
Author  :benni347:
"""


def read_file():
    """
    This reads the file.
    :return: a list of all ints in the given file.
    """
    filename: str = "input"
    with open(filename) as file:


    return local_content


def decimal_to_binary(decimal):
    """
    Converts a decimal to binary.
    Using https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/ example
    :type decimal: int
    :param decimal: a decimal value
    :return: the decimal value as a binary number
    """
    return bin(decimal).replace("0b", "")


def binary_to_decimal(binary):
    """
    Converts a binary to decimal
    :type binary: int
    :param binary: a binary number without 0b
    :return: the binary number in decimal
    """
    return int(str(binary), 2)



def binary_diagnostic_part_1(file_content: list):
    """
    To solve part 1 of the problem.
    :param file_content: a list with the directions of input.
    :return: the amount of differences.
    """
    length_of_string = len(file_content[0])
    gamma = [None] * length_of_string
    epsilon = [None] * length_of_string
    for i in range(length_of_string):
        zeros = sum(file_content[j][i] == "0" for j in range(len(file_content)))
        ones = sum(file_content[j][i] == "1" for j in range(len(file_content)))
        if zeros < ones:
            gamma[i] = "1"
            epsilon[i] = "0"
        else:
            gamma[i] = "0"
            epsilon[i] = "1"
        i += 1
    gamma = int("".join(gamma))
    epsilon = int("".join(epsilon))
    return binary_to_decimal(gamma) * binary_to_decimal(epsilon)



if __name__ == "__main__":
    content = read_file()
    PART_1 = binary_diagnostic_part_1(content)
    print(f"Part 1: {PART_1}")
