"""
This is the solution for part 2, its more readable in 2 files.
Author  :benni347@github.com
"""


def main():
    """
    The main function
    :return: the answer as an int
    """
    # Let's use proper bit operations now
    with open("./input", encoding="UTF8") as fin:
        data = fin.read().strip().split("\n")

    # Determine number of bits
    number_of_bits = len(data[0])

    data = [int(i, 2) for i in data]

    # Find oxygen
    o2 = data.copy()
    pos = number_of_bits - 1
    while pos >= 0 and len(o2) > 1:
        # Find the most common bit
        ones = sum(((x & (1 << pos)) >> pos) for x in o2)
        zeros = len(o2) - ones

        if zeros > ones:
            o2 = list(filter(lambda x: not (x & (1 << pos)), o2))
        else:
            o2 = list(filter(lambda x: (x & (1 << pos)), o2))

        pos -= 1

    # Find co2
    co2 = data.copy()
    pos = number_of_bits - 1
    while pos >= 0 and len(co2) > 1:
        # Find the most common bit
        ones = sum(((x & (1 << pos)) >> pos) for x in co2)
        zeros = len(co2) - ones

        if zeros > ones:
            co2 = list(filter(lambda x: (x & (1 << pos)), co2))
        else:
            co2 = list(filter(lambda x: not (x & (1 << pos)), co2))

        pos -= 1

    ans = o2[0] * co2[0]
    return ans


if __name__ == "__main__":
    part2 = main()
    print(f"Part2: {part2}")
