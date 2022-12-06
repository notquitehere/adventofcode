from elves.ip_ops import IPOps

scores = [("rock", "a", "x"), ("paper", "b", "y"), ("scissors", "c", "z")]
outcome = {"lose": 0, "draw": 3, "win": 6}
strategy = {"x": "lose", "y": "draw", "z": "win"}

test_ip = IPOps("day2/test_ip.txt").ip
ip = IPOps("day2/ip.txt").ip

def score(item: str):
    return([scores.index(i)+1 for i in scores if item.lower() in i][0])

def part1(ip):
    tot = 0
    for i in ip:
        a, b = (score(x) for x in i.split(" "))
        result = b
        if a-b in [-1,2]:
            result += outcome["win"]
        elif a == b:
            result += outcome["draw"]
        else:
            result += outcome["lose"]
        
        tot += result
    return tot

def part2(ip):
    tot = 0
    for i in ip:
        a,b = i.split(" ")
        a = score(a)
        b = strategy[b.lower()]
        result = outcome[b]
        if b == "win":
            result += (a % 3) + 1
        elif b == "draw":
            result += a
        else:
            result += ( a - 1 ) if a - 1 > 0 else 3
        tot += result
    return tot
    
print(part1(ip))
print(part2(ip))
