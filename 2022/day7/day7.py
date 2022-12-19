from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict
from elves.ip_ops import IPOps

test_ip = IPOps('day7/test_ip.txt').ip
ip = IPOps('day7/ip.txt').ip


@dataclass
class construct_data:
    """Dataclass containing a dictionary of folder sizes"""
    folder_sizes: Dict[int, int]

    def __init__(self, ip: list) -> None:
        """Construct folder sizes from the input instructions"""
        folder_sizes: Dict[int, int] = defaultdict(int)
        file_stack: List[int] = []

        for i in range(len(ip)):
            if not any([j for j in ["$", "dir"] if j in ip[i]]):
                file_size = int(ip[i].split(" ")[0])
                for folder in file_stack:
                    folder_sizes[folder] += file_size
            elif ".." in ip[i]:
                file_stack.pop()
            elif ip[i].split(" ")[1] == "cd":
                if "/" in ip[i]:
                    file_stack = []
                file_stack.append(i)
        
        self.folder_sizes = folder_sizes

def part1():
    return sum([i for i in folder_sizes.values() if i <= 100000])

def part2():
    disc_space = 70000000
    update_space = 30000000
    clear_space = update_space - (disc_space - folder_sizes[0])
    return min([i for i in folder_sizes.values() if i >= clear_space])

folder_sizes = construct_data(ip).folder_sizes
print(part1())
print(part2())