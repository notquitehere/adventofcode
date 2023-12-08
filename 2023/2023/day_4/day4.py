from pathlib import Path
import re


def get_ip(test: bool = False) -> list[str]:
    if test:
        return [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        ]

    ip_path = Path("2023/day_4/day4_ip.txt")
    with ip_path.open() as ip:
        return [i.strip() for i in ip.readlines()]


def part1(test: bool = False):
    cards = [re.split(r":|\|", i)[1:] for i in get_ip(test)]
    total = 0

    for winning, got in cards:
        winning_numbers = len(set([int(i) for i in winning.split()]) & set([int(i) for i in got.split()]))
        if winning_numbers == 0:
            continue

        points = 1
        for _ in range(winning_numbers-1):
            points += points

        total += points

    print(total)
    if test:
        assert total == 13


def part2(test: bool = False):
    cards = [re.split(r":|\|", i)[1:] for i in get_ip(test)]
    count = [1] * len(cards)
    for idx, card in enumerate(cards):
        winning, got = card
        winning_numbers = len(set([int(i) for i in winning.split()]) & set([int(i) for i in got.split()]))
        if winning_numbers == 0:
            continue

        for _ in range(count[idx]):
            start = idx+1
            for i in range(start, start+winning_numbers):
                count[i] += 1

    if test:
        assert sum(count) == 30

    print(sum(count))


if __name__ == "__main__":
    test = False
    part1(test)
    part2(test)
