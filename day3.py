from utils import read_file

tree_map = read_file('day3_input')

encounters = 0
x = 0

for line in tree_map[1:]:
    x = (x + 3) % (len(line))
    # print(f"{line[0:x]}[{line[x]}]{line[x+1:]}")
    if line[x] == "#":
        encounters += 1

print(encounters)