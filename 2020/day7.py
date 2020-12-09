with open('day7_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
           "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
           "bright white bags contain 1 shiny gold bag.",
           "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
           "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
           "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
           "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
           "faded blue bags contain no other bags.",
           "dotted black bags contain no other bags."]


def contains_gold(data, colour):
    answer = []
    d = []
    for l in data:
        contains = l.split(" ", 2)[-1]
        if colour in contains:
            answer.append(l)
        else:
            d.append(l)

    return answer, d


def p1recursive(data, colour):
    answer, d = contains_gold(data, colour)
    if not answer:
        return []
    else:
        for l in answer:
            colour = " ".join(l.split(" ", 2)[:2])
            ans, d = contains_gold(d, colour)
            answer.extend(ans)

        return answer


def part1(data):
    answer = set(p1recursive(data, "shiny gold"))

    print(answer)
    print(len(answer))


def gold_contains(data, colour):
    answer = []
    for l in data:
        if colour == " ".join(l.split(" ", 2)[:2]):
            answer.extend([i.strip(" .") for i in l.split("contain", 2)[-1].split(",")])

    return answer


def p2recursive(data, colour):
    contains = gold_contains(data, colour)

    if contains == ["no other bags"]:
        return 0
    else:
        total = 0
        for l in contains:
            elements = l.split(" ")
            number = int(elements[0])
            inside = p2recursive(data, " ".join(elements[1:3]))

            total += number + number * inside

        return total


def part2(data):
    total_bags = p2recursive(data, "shiny gold")
    print(f'total: {total_bags}')


if __name__ == "__main__":
    # part1(ip)
    part2(ip)

