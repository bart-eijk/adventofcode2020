from utils import read_file
import re

passwords = read_file('day2_input.txt')

regex_to_read_line = "(\d+)-(\d+) ([a-z]): ([a-z]+)"

valid_passwords = 0

for line in passwords:
    m = re.match(regex_to_read_line, line)
    first_spot = int(m.group(1))
    second_spot = int(m.group(2))
    letter = str(m.group(3))
    password = str(m.group(4))

    if (password[first_spot-1] == letter) ^ (password[second_spot-1] == letter):
        valid_passwords += 1

print(valid_passwords)

