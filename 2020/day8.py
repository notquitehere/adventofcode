with open('day8_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ["nop +0",
           "acc +1",
           "jmp +4",
           "acc +3",
           "jmp -3",
           "acc -99",
           "acc +1",
           "jmp -4",
           "acc +6"]


def part1(data):
    """
    - acc increases or decreases a single global value called the accumulator by the value given in the argument.
      For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction,
      the instruction immediately below it is executed next.
    - jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as
      an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to
      the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
    - nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
    """
    accumulator = 0
    executed = []
    prog_counter = 0

    while prog_counter not in executed and prog_counter < len(data):
        instruction, number = data[prog_counter].split(" ")
        previous_prog = int(prog_counter)

        if instruction == "nop":
            prog_counter += 1
        elif instruction == "acc":
            accumulator = accumulator + int(number)
            prog_counter += 1
        elif instruction == "jmp":
            prog_counter += int(number)

        executed.append(previous_prog)

    return accumulator, prog_counter


def part2(data):
    for i,l in enumerate(data):
        check_this = data.copy()
        instruction, num = l.split(" ")

        if instruction == "nop":
            check_this[i] = f"jmp {num}"
        elif instruction == "jmp":
            check_this[i] = f'nop {num}'

        accumulator, prog_counter = part1(check_this)

        if prog_counter >= len(data):
            return accumulator


if __name__ == "__main__":
    acc, loc = part1(ip)
    print(acc)
    print(part2(ip))
