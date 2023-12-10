from typing import Optional
from elves.elves import Elves
import re


def prep_ip(test: bool, ip_no: Optional[int] = None) -> tuple[list[str], dict[str, list[str]]]:
    ip = Elves.get_input(8, test)

    if ip_no is not None:
        ip = ip[ip_no]

    directions = list(ip[0])
    nodes = {}

    for l in ip[1:]:
        l = l.split("=")
        node = l[0].strip()
        nodes[node] = re.sub(r"\(|\)| ", "", l[-1]).split(",")

    return directions, nodes


def gcd(a: int, b: int) -> int:
    """Euclids algorithm."""
    if b == 0:
        return int(a)

    # ensures the numbers are the correct way round
    if b > a:
        a, b = b, a

    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """Lowest common multiplier."""
    # ensures the numbers are the correct way round
    if b > a:
        a, b = b, a

    return int(a * (b / gcd(a, b)))


def part1(test: bool, ip_no: Optional[int] = None):
    directions, nodes = prep_ip(test, ip_no)
    steps = 0
    location = "AAA"

    while location != "ZZZ":
        for dir in directions:
            steps += 1
            location = nodes[location][0 if dir == 'L' else 1]

    if test:
        assert steps in [2, 6]

    print(f"Part 1: {steps}")


def part2(test: bool):
    directions, nodes = prep_ip(test, 2 if test else None)
    locations = [i for i in list(nodes.keys()) if i.endswith("A")]

    for i in range(len(locations)):
        node = locations[i]
        steps = 0
        while not node.endswith("Z"):
            for dir in directions:
                steps += 1
                node = nodes[node][0 if dir == 'L' else 1]
        locations[i] = steps

    steps = 1
    for loc in locations:
        steps = lcm(steps, loc)

    if test:
        assert steps == 6

    print(f"Part 2: {steps}")


if __name__ == "__main__":
    test = False
    if test:
        part1(test, 0)
        part1(test, 1)
    else:
        part1(test)

    part2(test)
