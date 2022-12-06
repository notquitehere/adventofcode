from elves.ip_ops import IPOps

test_ip = IPOps('day4/test_ip.txt').ip
ip = IPOps('day4/ip.txt').ip

def _parse_line(i):
    return [set(list(range(int(a),int(b)+1))) for a,b in (j.split("-") for j in i.split(","))]

def part1(ip):
    pairs = 0
    for i in ip:
        elf1, elf2 = _parse_line(i)
        pairs += 1 if elf1.issubset(elf2) or elf2.issubset(elf1) else 0
    return pairs

def part2(ip):
    overlap = 0
    for i in ip:
        elf1, elf2 = _parse_line(i)
        if len(list(elf1 & elf2)) > 0:
            overlap += 1
    return overlap

# print(part1(ip))
print(part2(ip))
