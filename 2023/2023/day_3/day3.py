from pathlib import Path
import re


def get_ip(test: bool = False) -> list[str]:
    if test:
        return [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            ".......755",
            "...$..*...",
            ".664.598.."
        ]

    ip_path = Path("2023/day3/day3_ip.txt")
    with ip_path.open() as ip:
        return [i.strip() for i in ip.readlines()]


def part1(test: bool = False):
    ip = get_ip(test)
    rows = len(ip)
    total = 0

    for row in range(rows):
        part_numbers = re.findall(r"\d+", ip[row])
        row_start = row - 1 if row > 0 else 0
        row_end = row + 2 if row < rows else rows

        for n in set(part_numbers):
            locations = list(re.finditer(f"\\D?(?<![\\d]){n}(?![\\d])\\D?", ip[row]))
            for location in locations:
                start, end = location.span()

                adjacent_chars = [i[start:end] for i in ip[row_start:row_end]]
                if any(re.findall(r"[^\.\d\s]", chars) for chars in adjacent_chars):
                    total += int(n)

    if test:
        assert total == 4361

    print(total)


def part2(test: bool = False):
    ip = get_ip(test)
    rows = len(ip)
    total = 0

    for row in range(rows):
        row_start = row - 1 if row > 0 else 0
        row_end = row + 2 if row < rows else rows
        if len(gears := list(re.finditer(r"(.?\*.?)", ip[row]))) == 0:
            continue

        for gear in gears:
            start, end = gear.span()
            adjacent_chars = [i[start:end] for i in ip[row_start:row_end]]
            ratio = 1
            if sum([len(re.findall(r"\d+", chars)) for chars in adjacent_chars]) == 2:
                for row_ in range(row_start, row_end):
                    for number in list(re.finditer(r"\d+", ip[row_])):
                        num_start, num_stop = number.span()
                        if start <= num_start < end or start < num_stop < end:
                            ratio *= int(number.group())
                total += ratio

    if test:
        assert total == 467835

    print(total)


if __name__ == "__main__":
    test = False
    part1(test)
    part2(test)
