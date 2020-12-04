def valid1(passports):
    valid = []
    for p in passports:
        if (len(p) == 7 and 'cid' not in p) or (len(p) == 8):
            valid.append(p)
    return valid

def valid2(passports):
    valid_old = valid1(passports)
    valid_new = []
    for p in valid_old:
        try:
            byr = int(p['byr'])
            iyr = int(p['iyr'])
            eyr = int(p['eyr'])
            pid = p['pid']
            if (byr < 1920 or byr > 2002)\
            or (iyr < 2010 or iyr > 2020)\
            or (eyr < 2020 or eyr > 2030)\
            or (not pid.isnumeric() or len(pid) != 9):
                continue
        except:
            continue

        hgt = p['hgt']
        unit = hgt[-2:]
        try:
            height = int(hgt[:-2])
        except:
            continue
        if (unit == 'cm' and (height < 150 or height > 193))\
        or (unit == 'in' and (height < 59 or height > 76))\
        or not ((unit == 'in') ^ (unit == 'cm')):
            continue

        hcl = p['hcl']
        alphas = sum([c.isalpha() for c in hcl[1:]])
        digits = sum([c.isdigit() for c in hcl[1:]])
        if (hcl[0] != '#') or (alphas+digits != 6):
            continue

        colors = {'amb':'', 'blu':'', 'brn':'', 'gry':'', 'grn':'', 'hzl':'', 'oth':''}
        if (len(p['ecl']) != 3) or (p['ecl'] not in colors):
            continue


        valid_new.append(p)
    return valid_new


def read_input(filename):
    passports = []
    with open(filename, "r") as input:
        passport = {}
        for line in input:
            fields = line.strip()
            if fields == '':
                passports.append(passport)
                passport = {}
                continue
            entries = fields.split()
            for entry in entries:
                key, value = entry.split(":")
                passport[key] = value
        else:
            passports.append(passport)
    return passports


if __name__ == '__main__':
    passports = read_input("input.txt")
    print("(1) Valid passports:", len(valid1(passports)))
    print("(2) Valid passports:", len(valid2(passports)))
