from typing import List
from elves.ip_ops import IPOps

test_ip = IPOps("day5/test_ip.txt").ip
ip = IPOps("day5/ip.txt").ip

def _initial_locs(ip):
    cols = []
    for i in ip:
        if len(i) == 0:
            break
        
        rows = [i[j+1] for j in range(0, len(i), 4)]

        if len(cols) == 0:
            cols = [[] for r in range(0, len(rows))]
        
        for k in range(0, len(rows)):
            if rows[k] != " ":
                cols[k].insert(0, rows[k])

    return cols

def _instructions(ip: List[List[str]]) -> List[List[int]]:
    """returns a 2d list of instructions:
    
    Args:
        ip List[List[str]]: 2d representation of puzzle input
    
    Returns:
        List[List[int]]: 2d representation of movement instructions. Each sublist contains the following values
                         [<quantity>, <from>, <to>]
    """
    inst = []
    for i in ip:
        if "move" not in i:
            continue
        
        inst.append([int(j) for j in i.split(" ") if j.isdigit()])
    
    return(inst)

def part1(ip):
    piles = _initial_locs(ip)

    for inst in _instructions(ip):
        qty, start, end = inst
        for _ in range(qty):
            piles[end-1].append(piles[start-1].pop())
    
    return "".join([pile.pop() for pile in piles])

def part2(ip):
    piles = _initial_locs(ip)

    for inst in _instructions(ip):
        qty, start, end = inst
        piles[end-1].extend(piles[start-1][-qty:])
        piles[start-1] = piles[start-1][:-qty]

    return "".join([pile.pop() for pile in piles if len(pile) > 1])
    
# print(part1(ip))
print(part2(ip))