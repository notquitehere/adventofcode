from typing import List
from elves.ip_ops import IPOps

test_ip = IPOps("day1/test_ip.txt").ip
puzzle_ip = IPOps("day1/ip.txt").ip

elf_cals = []

def part1(ip):
    elf_calc = 0
    for i in ip:
        if i == "":
            elf_cals.append(elf_calc)
            elf_calc = 0
        else:
            elf_calc += int(i)
    
    elf_cals.append(elf_calc)

    return(max(elf_cals))

def part2():
    elf_cals.sort()
    return sum(elf_cals[-3:])

print(part1(puzzle_ip))
print(part2())
