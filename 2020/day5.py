from math import ceil

# load the input
with open('day5_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ["FBFBBFFRLR",  # Row 44, column 5 id 357
           "BFFFBBFRRR",  # row 70, column 7, seat ID 567.
           "FFFBBBFRRR",  # row 14, column 7, seat ID 119.
           "BBFFBBFRLL"]  # row 102, column 4, seat ID 820.


def find_location(data, start, stop):
    if len(data) == 1:
        d = data[0]
        if d == 'F' or d == 'L':
            return start + ((stop - start) // 2)
        else:
            return start + ceil((stop - start) / 2)

    d = data.pop(0)

    if d == "F" or d == "L":
        stop = start + ((stop - start) // 2)
    else:
        start += ceil((stop - start) / 2)

    return find_location(data, start, stop)


def part1(data):
    # rows = 0 - 127
    # cols = 0 - 7
    max_seat_id = -1
    for line in data:
        row = find_location(list(line[:7]), 0, 127)
        col = find_location(list(line[7:]), 0, 7)
        max_seat_id = max(max_seat_id, row * 8 + col)

    return max_seat_id


def part2(data):
    seats = []
    for line in data:
        row = find_location(list(line[:7]), 0, 127)
        col = find_location(list(line[7:]), 0, 7)
        seats.append(row * 8 + col)

    actual_seats = set(seats)
    theoretical_seats = set([*range(min(seats),max(seats))])

    return theoretical_seats.difference(actual_seats)


if __name__ == "__main__":
    print(part1(ip))
    print(part2(ip))