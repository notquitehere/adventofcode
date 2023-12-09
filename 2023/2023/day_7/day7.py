from elves.elves import Elves
from collections import Counter


def quicksort(array: list, low: int, high: int, part: int):
    # ensure indices are in the correct order
    if low >= high or low < 0:
        return

    # partition array and get the pivot index
    p = partition(array, low, high, part)

    # sort the two partitions
    quicksort(array, low, p-1, part)
    quicksort(array, p+1, high, part)


def partition(array: list, low: int, high: int, part: int) -> int:
    # take the last element as the pivot
    pivot = array[high][0]

    # set a temporary pivot index
    i = low - 1

    for j in range(low, high):
        comparision = compare_p1(array[j][0], pivot) if part == 1 else compare_p2(array[j][0], pivot)
        if comparision:
            i += 1
            array[i], array[j] = array[j], array[i]

    # move the pivot element to the correct position
    i += 1
    array[i], array[high] = array[high], array[i]
    return i


def compare_p1(hand_a: str, hand_b: str) -> bool:
    strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    counter_a, counter_b = Counter(hand_a), Counter(hand_b)

    if max(counter_a.values()) != max(counter_b.values()):
        return max(counter_a.values()) < max(counter_b.values())

    if len(counter_a.values()) != len(counter_b.values()):
        return len(counter_a.values()) > len(counter_b.values())

    for card_a, card_b in (zip(list(hand_a), list(hand_b))):
        if card_a != card_b:
            return strength.index(card_a) > strength.index(card_b)

    # hands are equal
    return False

def compare_p2(hand_a: str, hand_b: str) -> bool:
    strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def _jokers(hand: str):
        counter = Counter(hand)

        if "J" not in hand or hand == "JJJJJ":
            return list(counter.values())

        jays = counter.pop("J")

        counter = sorted(list(counter.values()))
        counter[-1] += jays
        return counter

    counter_a, counter_b = _jokers(hand_a), _jokers(hand_b)

    if max(counter_a) != max(counter_b):
        return max(counter_a) < max(counter_b)

    if len(counter_a) != len(counter_b):
        return len(counter_a) > len(counter_b)

    for card_a, card_b in (zip(list(hand_a), list(hand_b))):
        if card_a != card_b:
            return strength.index(card_a) > strength.index(card_b)

    # hands are equal
    return False


def part1(test: bool):
    ip = [i.split() for i in Elves.get_input(7, test)]
    total = 0

    quicksort(ip, 0, len(ip)-1, 1)

    if test:
        assert ip == [['32T3K', '765'], ['KTJJT', '220'], ['KK677', '28'], ['T55J5', '684'], ['QQQJA', '483']]

    for idx, hand in enumerate(ip):
        total += int(hand[1]) * (idx + 1)

    if test:
        assert total == 6440

    print(total)


def part2(test: bool):
    ip = [i.split() for i in Elves.get_input(7, test)]
    total = 0

    quicksort(ip, 0, len(ip)-1, 2)

    if test:
        assert ip == [['32T3K', '765'], ['KK677', '28'], ['T55J5', '684'], ['QQQJA', '483'], ['KTJJT', '220']]

    for idx, hand in enumerate(ip):
        total += int(hand[1]) * (idx + 1)

    if test:
        assert total == 5905

    print(total)


if __name__ == "__main__":
    test = False
    # part1(test)
    part2(test)