from utils import read_file

def count_trees(right:int, down:int, treemapfile:str):
    tree_map = read_file(treemapfile)

    encounters = 0
    x = 0
    skip = down

    # print(tree_map[0])
    for n in range(1, len(tree_map)):
        line = tree_map[n]
        if skip != 1:
            skip -= 1
            # print(line)
            continue
        skip = down
        x = (x + right) % (len(line))
        # print(f"{line[0:x]}[{line[x]}]{line[x+1:]}")
        if line[x] == "#":
            encounters += 1
    # print("\n")

    return encounters


def test():
    assert count_trees(1, 1, "day3_testinput") == 2
    assert count_trees(3, 1, "day3_testinput") == 7
    assert count_trees(5, 1, "day3_testinput") == 3
    assert count_trees(7, 1, "day3_testinput") == 4
    assert count_trees(1, 2, "day3_testinput") == 2

print(count_trees(1, 1, "day3_input") *
      count_trees(3, 1, "day3_input") *
      count_trees(5, 1, "day3_input") *
      count_trees(7, 1, "day3_input") *
      count_trees(1, 2, "day3_input")
      )
