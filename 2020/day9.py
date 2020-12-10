with open('day9_ip.txt', 'r') as f:
    ip = [int(i.strip('\n')) for i in f]

test_ip = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]


def part1(data, preamble_len):
    for i, n in enumerate(data[preamble_len:], start=preamble_len):
        sum_of = data[i-preamble_len:i]
        is_a_sum = 0
        for m in sum_of:
            if n - m in sum_of:
                is_a_sum = 1
        if not is_a_sum:
            return n


def part2(data, preamble_len):
    find = part1(data, preamble_len)
    for i, n in enumerate(data):
        total = n
        current_number = i
        while total < find:
            current_number += 1
            total += data[current_number]

        if total == find:
            sums_to_find = data[i:current_number+1]
            return min(sums_to_find) + max(sums_to_find)


if __name__ == "__main__":
    # print(part1(ip, 25))
    print(part2(ip, 25))