from elves.elves import Elves


def part1(test: bool):
    ip = Elves.get_input(6, test)
    ip = [i.split(":")[-1].split() for i in ip]
    races = zip(ip[0], ip[1])
    margin = None

    for race in races:
        time, distance = [int(i) for i in race]
        possible = 0
        for i in range(1, int(time/2)+1):
            if i * (time - i) > distance:
                possible += 1

        possible = possible * 2 if time % 2 != 0 else (possible * 2) - 1
        margin = margin * possible if margin is not None else possible

    print(margin)

    if test:
        assert margin == 288


def part2(test: bool):
    ip = Elves.get_input(6, test)
    time, distance = [int(i.split(":")[-1].replace(" ", "")) for i in ip]
    possible = 0
    for i in range(1, int(time/2)+1):
        if i * (time - i) > distance:
            possible += 1

    print(possible)
    possible = possible * 2 if time % 2 != 0 else (possible * 2) - 1

    print(possible)

    if test:
        assert possible == 71503


if __name__ == "__main__":
    test = False
    # part1(test)
    part2(test)
