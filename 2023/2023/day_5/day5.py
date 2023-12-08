from ..elves.elves import get_input


def part1(test: bool):
    ip = get_input(5, test)
    closest = None
    seeds = [int(i) for i in ip[0].split(":")[-1].split()]
    maps = []

    for line in ip[1:]:
        if "map" in line:
            maps.append([])
            continue
        maps[-1].append([int(i) for i in line.split()])

    for seed in seeds:
        next = seed
        for map in maps:
            for m in map:
                to_, from_, count_ = m
                if from_ <= next < from_ + count_:
                    next = next + to_ - from_
                    break

        if closest is None or next < closest:
            closest = next

    print(closest)


def part2(test: bool):
    ip = get_ip(test)
    closest = None
    seeds = [int(i) for i in ip[0].split(":")[-1].split()]
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    maps = []

    for line in ip[1:]:
        if "map" in line:
            maps.append([])
            continue
        maps[-1].append([int(i) for i in line.split()])

    for seed_start, seed_end in seeds:
        for s in range(seed_start, seed_start + seed_end):
            next = s
            for map in maps:
                for m in map:
                    to_, from_, count_ = m
                    if from_ <= next < from_ + count_:
                        next = next + to_ - from_
                        break

            if closest is None or next < closest:
                closest = next

    print(closest)


if __name__ == "__main__":
    test = False
    # part1(test)
    part2(test)
