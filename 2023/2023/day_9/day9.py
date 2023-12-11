from elves.elves import Elves


def next_val(seq: list[int], tot: int = 0) -> int:
    diffs = []
    tot += seq[-1]
    for a, b in zip(seq, seq[1:]):
        diffs.append(b-a)

    if len(set(diffs)) == 1:
        return tot + diffs[-1]

    return next_val(diffs, tot)


def prev_val(seq: list[int]) -> int:
    diffs = []
    for a, b in zip(seq, seq[1:]):
        diffs.append(b-a)

    if len(set(diffs)) == 1:
        return seq[0] - diffs[0]

    return seq[0] - prev_val(diffs)


def part1(test: bool):
    ip = Elves.get_input(9, test)
    total = 0

    for i in ip:
        vals = [int(j) for j in i.split()]
        total += next_val(vals)

    if test:
        assert total == 114

    print(total)


def part2(test: bool):
    ip = Elves.get_input(9, test)
    total = 0

    for i in ip:
        vals = [int(j) for j in i.split()]
        total += prev_val(vals)

    if test:
        assert total == 2

    print(total)


if __name__ == "__main__":
    test = False
    part1(test)
    part2(test)
