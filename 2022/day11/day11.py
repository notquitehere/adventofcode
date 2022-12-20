from math import floor, prod
from functools import reduce
from elves.ip_ops import IPOps

test_ip = IPOps('day11/test_ip.txt').ip
ip = IPOps('day11/ip.txt').ip

def _process_ip(ip):
    monkeys = {}
    for i in range(0,len(ip),7):
        if (m := ip[i].strip(":").split(" "))[0] == "Monkey":
            test = [int(ip[i+x].split(" ")[-1]) for x in range(3,6)]
            monkey = {
                "items": [int(item.strip()) for item in ip[i+1].split(":")[-1].split(",")],
                "op": ip[i+2].split("=")[-1].strip(),
                "test": test,
                "total": 0
            }
            monkeys[m[-1]] = monkey
    return monkeys

def part1(ip):
    monkeys = _process_ip(ip)
    for _ in range(20):
        for monkey in monkeys.values():
            for item in monkey["items"]:
                worry = floor(eval(monkey["op"].replace("old", f"{item}")) / 3)
                throw_to = monkey["test"][1]  if worry % monkey["test"][0] == 0 else monkey["test"][2]
                monkeys[f"{throw_to}"]["items"].append(worry)
                monkey["total"] += 1
            monkey["items"] = []

    monkey_business = reduce(lambda x,y: x*y, sorted([monkey["total"] for monkey in monkeys.values()])[-2:])
    print(monkey_business)

def part2(ip):
    monkeys = _process_ip(ip)
    enhance_calm = prod([m["test"][0] for m in monkeys.values()])
    for _ in range(10000):
        for monkey in monkeys.values():
            for item in monkey["items"]:
                worry = eval(monkey["op"].replace("old", f"{item}")) % enhance_calm
                throw_to = monkey["test"][1]  if worry % monkey["test"][0] == 0 else monkey["test"][2]
                monkeys[f"{throw_to}"]["items"].append(worry)
                monkey["total"] += 1
            monkey["items"] = []

    monkey_business = reduce(lambda x,y: x*y, sorted([monkey["total"] for monkey in monkeys.values()])[-2:])
    print(monkey_business)

part1(ip)
part2(ip)