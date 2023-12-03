from functools import reduce
from pathlib import Path


def get_ip(test: bool = False) -> list[str]:
    if test:
        return [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]

    ip_path = Path("2023/day2/day2_ip.txt")
    with ip_path.open() as ip:
        return ip.readlines()


def part1(test: bool = False):
    ip = get_ip(test)
    bag_contents = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    total = 0

    for line in ip:
        id, tries = line.split(":")
        tries = [i.split() for i in tries.replace(";", ",").split(",")]
        if not any(int(try_[0]) > bag_contents[try_[1]] for try_ in tries):
            total += int(id.split()[-1])

    print(total)


def part2(test: bool = False):
    ip = get_ip(test)
    total = 0

    for line in ip:
        tries = line.split(":")[-1]
        min_contents = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for num, colour in [i.split() for i in tries.replace(";", ",").split(",")]:
            if min_contents[colour] < int(num):
                min_contents[colour] = int(num)

        total += reduce(lambda x, y: x*y, min_contents.values())

    print(total)


if __name__ == "__main__":
    test = False
    # part1(test)
    part2(test)
