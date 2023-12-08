from pathlib import Path


def get_input(day: int, test: bool = False):
    test_ip = ["", "", "", "",
               [
                    "seeds: 79 14 55 13",
                    "seed-to-soil map:",
                    "50 98 2",
                    "52 50 48",
                    "soil-to-fertilizer map:",
                    "0 15 37",
                    "37 52 2",
                    "39 0 15",
                    "fertilizer-to-water map:",
                    "49 53 8",
                    "0 11 42",
                    "42 0 7",
                    "57 7 4",
                    "water-to-light map:",
                    "88 18 7",
                    "18 25 70",
                    "light-to-temperature map:",
                    "45 77 23",
                    "81 45 19",
                    "68 64 13",
                    "temperature-to-humidity map:",
                    "0 69 1",
                    "1 0 69",
                    "humidity-to-location map:",
                    "60 56 37",
                    "56 93 4"
                ], [
                    "Time:      7  15   30",
                    "Distance:  9  40  200"
                ]]
    if test:
        return test_ip[day-1]

    ip_path = Path(f"2023/day_{day}/day{day}_ip.txt")
    with ip_path.open() as ip:
        return [i.strip() for i in ip.readlines() if len(i.strip()) > 0]
