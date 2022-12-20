from typing import List
from elves.ip_ops import IPOps

test_ip = IPOps('day10/test_ip.txt').ip
ip = IPOps('day10/ip.txt').ip

def part1(ip: List) -> None:
    instruction, cycle, register = 0, 1, 1
    strengths = []

    def _interesting(c: int):
        if c % 20 == 0 and not c % 40 == 0:
            print(c, register)
            strengths.append(c * register)

    while cycle < 221 and instruction < len(ip):
        _interesting(cycle)
    
        if ip[instruction].strip() == "noop":
            cycle += 1
        else:
            _interesting(cycle+1)
            register += int(ip[instruction].split(" ")[-1])
            cycle += 2
        
        instruction += 1

    print(sum(strengths))

def part2(ip: List) -> None:
    instruction, cycle, register = 0, 0, 1
    crt = []

    def _pixel(c: int):
        row, c = int(c / 40), c % 40

        # ensure there is a list for the row of the crt
        if row == len(crt):
            crt.append([])

        if c in range(register-1, register+2):
            crt[row].append("#")
        else:
            crt[row].append(".")

    while cycle < 241 and instruction < len(ip):
        row = int(cycle / 40)
        
        _pixel(cycle)

        if ip[instruction].strip() == "noop":
            cycle += 1
        else:
            _pixel(cycle+1)
            register += int(ip[instruction].split(" ")[-1])
            cycle += 2
        
        instruction += 1
    
    for i in crt:
        print("".join(i))


# part1(ip)
part2(ip)