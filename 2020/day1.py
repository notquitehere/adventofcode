# load the puzzle input
with open('day1_ip.txt', 'r') as f:
    ip = [int(i.strip('\n')) for i in f]

test_ip = [1721, 979, 366, 299, 675, 1456]


def part1(nums):
    while len(nums) > 0:
        first_num = nums.pop(0)
        for i in nums:
            if first_num + i == 2020:
                print(f'{first_num} + {i} = 2020')
                return first_num * i


def part2(nums):
    while len(nums) > 2:
        first_num = nums.pop(0)
        for i in nums:
            for j in nums[1:]:
                if first_num + i + j == 2020:
                    print(f'{first_num} + {i} + {j} = 2020')
                    return first_num * i * j


print(part2(ip))