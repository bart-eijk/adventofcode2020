import re

def check_hgt(x):
    m = re.match("(\d*)([a-z]*)", x)
    if not m or len(m.groups()) != 2:
        return False

    groups = m.groups()

    if groups[1] == "cm":
        return 150 <= int(groups[0]) <= 193
    elif groups[1] == "in":
        return 59 <= int(groups[0]) <= 76
    else:
        return False


fields_and_checks = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": check_hgt,
    "hcl": lambda x: bool(re.match("#[0-9a-f]{6}", x)),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: bool(re.match("^[0-9]{9}$", x)),
}

with open('day4_input.txt') as f:
    lines = f.read()

valid_count = 0
for passport in lines.split("\n\n"):
    if not all(rf in passport for rf in [r + ":" for r in fields_and_checks.keys()]):
        continue
    fields_and_content = dict(re.findall("([a-z]{3}):([a-z0-9#]*)[\s\n]?", passport))
    print(fields_and_content)

    valid = True
    for fieldname, check_function in fields_and_checks.items():
        if not valid:
            continue
        val_to_check = fields_and_content[fieldname]
        outcome = check_function(val_to_check)
        print(f"Checking {fieldname}={val_to_check}. Outcome=[{outcome}]")
        if not check_function(val_to_check):
            valid = False

    if valid:
        valid_count += 1

print(valid_count)