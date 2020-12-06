# load input
with open('day6_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ["abc",
           "",
           "a",
           "b",
           "c",
           "",
           "ab",
           "ac",
           "",
           "a",
           "a",
           "a",
           "a",
           "",
           "b"]


def part1(data):
    groups = [set()]

    for l in data:
        if l == "":
            groups.append(set())
        else:
            groups[len(groups)-1].update(*list(l))

    return sum([len(i) for i in groups])


def part2(data):
    groups = [set()]
    start = 0

    for i, l in enumerate(data):
        if l == "":
            groups.append(set())
            start = i
        elif i == 0 or i == start+1:
            groups[len(groups)-1].update(*list(l))
        else:
            groups[len(groups)-1] = groups[len(groups)-1].intersection(set(list(l)))

    return sum([len(i) for i in groups])


if __name__ == "__main__":
    print(part1(ip))
    print(part2(ip))