from functools import reduce

# Load the puzzle input
with open('day3_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ['..##.......',
           '#...#...#..',
           '.#....#..#.',
           '..#.#...#.#',
           '.#...##..#.',
           '..#.##.....',
           '.#.#.#....#',
           '.#........#',
           '#.##...#...',
           '#...##....#',
           '.#..#...#.#']


def part1(data, right, down):
    line_len = len(data[0])
    location = 0
    trees = 0
    for l in range(0,len(data),down):
        if data[l][location] == '#':
            trees += 1
        location = (location + right) % line_len


    return trees


def part2(data):
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    trees = 1

    for s in slopes:
        trees *= part1(data, s[0], s[1])

    return trees


if __name__ == "__main__":
    print(f'Part One Solution: {part1(ip, 3, 1)}')
    print(f'Part Two Solution: {part2(ip)}')
