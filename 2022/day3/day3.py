from elves.ip_ops import IPOps
import string

test_ip = IPOps("day3/test_ip.txt").ip
ip = IPOps("day3/ip.txt").ip
locations = string.ascii_lowercase + string.ascii_uppercase

def part1(ip):
    dups = []
    for i in ip:
        half_way = int(len(i)/2)
        dups.append(set([j for j in i[:half_way] if j in i[half_way:]]))

    
    return sum([locations.index(list(i)[0])+1 for i in dups if len(i) > 0])

def part2(ip):
    tot = 0
    for i in range(0, len(ip), 3):
        tot += locations.index(list(set(ip[i]) & set(ip[i+1]) & set(ip[i+2]))[0])+1
    return tot

print(part1(ip))
print(part2(ip))