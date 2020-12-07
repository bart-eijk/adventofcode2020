required_fields = [
    "byr:",
    "iyr:",
    "eyr:",
    "hgt:",
    "hcl:",
    "ecl:",
    "pid:",
]

with open('day4_input.txt') as f:
    lines = f.read()

valid_count = 0
for passport in lines.split("\n\n"):
    if all(rf in passport for rf in required_fields):
        valid_count += 1

print(valid_count)