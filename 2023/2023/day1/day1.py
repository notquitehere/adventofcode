from pathlib import Path
import re


ip = Path("2023/day1/day1_ip.txt")


def calc(lines: list[str]) -> int:
    tot = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        tot += int(f"{digits[0]}{digits[-1]}")
    return tot


def part_1():
    with ip.open() as coords:
        print(f"part1: {calc(coords.readlines())}")


def part_2():
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with ip.open() as coords:
        lines = coords.readlines()
        for i in range(len(lines)):
            for n in numbers:
                lines[i] = lines[i].replace(n, f"{n[0]}{numbers.index(n)+1}{n[-1]}")
        print(f"part2: {calc(lines)}")


if __name__ == "__main__":
    part_1()
    part_2()
