from elves.ip_ops import IPOps

test_ip = IPOps('day9/test_ip.txt').ip
p1 = test_ip[:9]
p2 = test_ip[10:]
ip = IPOps('day9/ip.txt').ip

def part1(ip):
    head, tail = [0,0], [0,0]
    tail_locs = [(0,0)]

    for i in ip:
        dir, dist = i.split(" ")

        for _ in range(int(dist)):
            if dir in ["R", "L"]:
                head[0] += 1 if dir == "R" else -1
            else:
                head[1] += 1 if dir == "U" else -1
            
            diffs = tuple(map(lambda a, b: abs(a - b), head, tail))
            
            if any([i > 1 for i in diffs]):
                if all([i > 0 for i in diffs]):
                    tail[0] += 1 if head[0] - tail[0] > 0 else -1
                    tail[1] += 1 if head[1] - tail[1] > 0 else -1
                elif diffs[0] > 0:
                    tail[0] += 1 if head[0] - tail[0] > 0 else -1
                else:
                    tail[1] += 1 if head[1] - tail[1] > 0 else -1
                
                tail_locs.append(tuple(tail))

    print(len(set(tail_locs)))


def part2(ip):
    knots = [[0,0] for _ in range(10)]
    tail_locs = []

    for i in ip:
        dir, dist = i.split(" ")
        for _ in range(int(dist)):
            # start the move with the head of the rope
            if dir in ["R", "L"]:
                knots[0][0] += 1 if dir == "R" else -1
            else:
                knots[0][1] += 1 if dir == "U" else -1
            
            for j in range(len(knots)-1):
                diffs = tuple(map(lambda a,b: abs(a-b), knots[j], knots[j+1]))

                if any([i > 1 for i in diffs]):
                    if all([i > 0 for i in diffs]):
                        knots[j+1][0] += 1 if knots[j][0] - knots[j+1][0] > 0 else -1
                        knots[j+1][1] += 1 if knots[j][1] - knots[j+1][1] > 0 else -1
                    elif diffs[0] > 0:
                        knots[j+1][0] += 1 if knots[j][0] - knots[j+1][0] > 0 else -1
                    else:
                        knots[j+1][1] += 1 if knots[j][1] - knots[j+1][1] > 0 else -1
                
                if j+2 == len(knots):
                    tail_locs.append(tuple(knots[-1]))
    print(len(set([tuple(i) for i in tail_locs])))

# part1(ip)
part2(ip)