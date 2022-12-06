from elves.ip_ops import IPOps

test_data = IPOps("day6/test_ip.txt")
ip = IPOps("day6/ip.txt").ip[0]


def solution(ip: str, marker_len: int):
    for i in range(len(ip)):
        if i+marker_len > len(ip):
            return "marker not found"
        if len(set(ip[i:i+marker_len])) == marker_len:
            return i+marker_len


# test
for i, item in enumerate(test_data.ip):
    # part1
    assert solution(item, 4) == int(test_data.exp_p1[i])
    # part2
    assert solution(item, 14) == int(test_data.exp_p2[i])

# part1
print(solution(ip, 4))
# part2
print(solution(ip, 14))