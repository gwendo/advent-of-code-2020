import re


def validate_password(passport):
    req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    fields = set(map(lambda f: f[0], passport))
    validation_result = list(map(lambda field: (validate_field(field), field), passport))
    print(validation_result)
    #
    return req_fields.issubset(fields) and all(map(lambda v: v[0], validation_result))


def byr(value):
    return 1920 <= int(value) <= 2002


def iyr(value):
    return 2010 <= int(value) <= 2020


def eyr(value):
    return 2020 <= int(value) <= 2030


def hgt(value):
    unit = value[-2:]

    return (unit == "cm" and 150 <= int(value[:-2]) <= 193) or (unit == "in" and 59 <= int(value[:-2]) <= 76)


def hcl(value):
    rule = re.compile("#[a-f0-9]{6,}$")
    match = rule.match(value)
    if match:
        return True
    else:
        return False


def ecl(value):
    colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return {value}.issubset(colors)


def pid(value):
    return len(value) == 9 and value.isnumeric()


def valid(value):
    return True


def validate_field(field):
    switcher = {
        "byr": byr,
        "iyr": iyr,
        "eyr": eyr,
        "hgt": hgt,
        "hcl": hcl,
        "ecl": ecl,
        "pid": pid,
        "cid": valid
    }
    func = switcher.get(field[0])
    return func(field[1])
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def count_valid_passwords(input):
    passports = extract_passwords(input)
    return list(map(validate_password, passports)).count(True)


def extract_passwords(input):
    passports = []
    curr_passport = []
    for l in input:
        if len(l) == 0:
            passports.append(curr_passport)
            curr_passport = []
        else:
            curr_passport.extend(map(lambda f: (f[0], f[1]), map(lambda field: field.split(":"), l.split(" "))))

    passports.append(curr_passport)
    return passports
