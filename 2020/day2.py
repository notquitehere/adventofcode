from collections import Counter

# Load the puzzle input
with open('day2_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']


def split_it(data):
    num, ch, string = data.split(' ')
    num1, num2 = num.split('-')

    return int(num1), int(num2), ch.strip(':'), string


def part1(data):
    valid = 0
    for l in data:
        num1, num2, ch, string = split_it(l)
        if Counter(string)[ch] in range(num1, num2+1):
            valid += 1

    return valid


def part2(data):
    valid = 0
    for l in data:
        num1, num2, ch, string = split_it(l)
        if (string[num1-1] == ch or string[num2-1] == ch) and not (string[num1-1] == ch and string[num2-1] == ch):
            valid += 1

    return valid


if __name__ == '__main__':
    print(part1(ip))
    print(part2(ip))