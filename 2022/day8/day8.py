from elves.ip_ops import IPOps

test_ip = IPOps("day8/test_ip.txt").ip
test_ip = [[int(j) for j in list(i)] for i in test_ip]

ip = IPOps('day8/ip.txt').ip
ip = [[int(j) for j in list(i)] for i in ip]

def _rows_n_cols(ip):
    return ip, [list(i) for i in list(zip(*ip))]

def _visible(ip):
    visible = []
    for i in range(len(ip)):
        len_x, len_y = len(ip[i]), len(ip)
        if i == 0 or i == len_y-1:
            visible.append(list("v" * len_x))
        else:
            row = []
            for j in range(len_x):
                if j == 0 or j == len_x-1:
                    row.append("v")
                else:
                    this_row = ip[i]

                    if all([t < this_row[j] for t in this_row[:j]]) or all([t < this_row[j] for t in this_row[j+1:]]):
                        row.append("v")
                    else:
                        row.append("x")
            visible.append(row)
    return visible

def _viewing_distance(ip):
    distance = []
    for i in range(len(ip)):
        if i == 0 or i == len(ip)-1:
            distance.append([0 for _ in range(len(ip[i]))])
        else:
            row = []
            for j in range(len(ip[i])):
                def _next(lst):
                    try:
                        return next(idx for idx, val in enumerate(lst) if val >= ip[i][j]) + 1
                    except StopIteration:
                        return len(lst)
                left, right = ip[i][:j], ip[i][j+1:]
                row.append(_next(left[::-1]) * _next(right))
            distance.append(row)
    
    return distance
                

def part1(ip):
    rows, cols = _rows_n_cols(ip)
    visible = list(zip(_visible(rows), [list(i) for i in list(zip(*_visible(cols)))]))
    total_visible = 0
    for v in visible:
        is_vis = list(zip(*v))
        for t in is_vis:
            if 'v' in t:
                total_visible += 1
    print(total_visible)

def part2(ip):
    rows, cols = _rows_n_cols(ip)
    scenic_scores = list(zip(_viewing_distance(rows), [list(i) for i in list(zip(*_viewing_distance(cols)))]))
    most_scenic = 0
    for i in scenic_scores:
        max_in_row = max([j[0]*j[1] for j in list(zip(*i))])
        if max_in_row > most_scenic:
            most_scenic = max_in_row
    return most_scenic

# part1(ip)
print(part2(ip))
