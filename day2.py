from utils import read_file
import re

passwords = read_file('day2_input.txt')

regex_to_read_line = "(\d+)-(\d+) ([a-z]): ([a-z]+)"

valid_passwords = 0

for line in passwords:
    m = re.match(regex_to_read_line, line)
    min_occurs = int(m.group(1))
    max_occurs = int(m.group(2))
    letter = m.group(3)
    password = m.group(4)

    if min_occurs <=  password.count(letter) <= max_occurs:
        valid_passwords += 1

print(valid_passwords)

