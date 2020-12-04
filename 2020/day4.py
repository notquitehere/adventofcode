import re

# load the input
with open('day4_ip.txt', 'r') as f:
    ip = [i.strip('\n') for i in f]

test_ip = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
           "byr:1937 iyr:2017 cid:147 hgt:183cm",
           "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
           "hcl:#cfa07d byr:1929",
           "",
           "hcl:#ae17e1 iyr:2013",
           "eyr:2024",
           "ecl:brn pid:760753108 byr:1931",
           "hgt:179cm",
           "",
           "hcl:#cfa07d eyr:2025 pid:166559648",
           "iyr:2011 ecl:brn hgt:59in"]

invalid_ip = ["eyr:1972 cid:100",
              "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
              "",
              "iyr:2019",
              "hcl:#602927 eyr:1967 hgt:170cm",
              "ecl:grn pid:012533040 byr:1946",
              "",
              "hcl:dab227 iyr:2012",
              "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
              "",
              "hgt:59cm ecl:zzz",
              "eyr:2038 hcl:74454a iyr:2023",
              "pid:3556412378 byr:2007"]

valid_ip = ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
            "hcl:#623a2f",
            "",
            "eyr:2029 ecl:blu cid:129 byr:1989",
            "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            "",
            "hcl:#888785",
            "hgt:164cm byr:2001 iyr:2015 cid:88",
            "pid:545766238 ecl:hzl",
            "eyr:2022"]

codes = {"byr": "Birth Year",
         "iyr": "Issue Year",
         "eyr": "Expiration Year",
         "hgt": "Height",
         "hcl": "Hair Color",
         "ecl": "Eye Color",
         "pid": "Passport ID",
         "cid": "Country ID"}


def make_dict(data):
    passports = [{}]
    for l in data:
        if len(l) == 0:
            passports.append(dict())
        else:
            items = l.split(' ')
            for i in items:
                kv = i.split(':')
                passports[-1][kv[0]] = kv[1]
    return passports


def is_valid(passport):
    passport_codes = set(codes.keys())
    diff = passport_codes.difference(set(passport.keys()))
    if len(diff) == 0:
        return 1
    elif len(diff) == 1 and 'cid' in diff:
        return 1
    return 0


def part1(data):
    valid = 0
    for i in data:
        valid += is_valid(i)

    return valid


def part2(data):
    """
    Criteria for a passport to be valid p2:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    valid = 0
    eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hair_colour = re.compile("#[a-f0-9]{6}")
    passport_num = re.compile("[0-9]{9}")
    for i in data:
        v = 0
        if is_valid(i):
            if int(i['byr']) in range(1920,2003) and int(i['iyr']) in range(2010,2021)\
                    and int(i['eyr']) in range(2020,2031) and i['ecl'] in eye_colours\
                    and hair_colour.match(i['hcl']) and passport_num.match(i['pid']) and len(i['pid']) == 9:
                v += 1

            height_range = i['hgt'][-2:]
            if height_range == 'cm' and int(i['hgt'][:-2]) in range(150,194):
                v += 1
            elif height_range == 'in' and int(i['hgt'][:-2]) in range(59,77):
                v += 1

        if v == 2:
            valid += 1

    return valid


if __name__ == "__main__":
    passport_data = make_dict(ip)
    print(part1(passport_data))
    print(part2(passport_data))