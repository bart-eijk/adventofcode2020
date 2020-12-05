numbers = [int(line.strip()) for line in open('day1_input.txt')]
for i in numbers:
    for j in numbers:  # this is O(n^2), but let's make it work
        if i + j == 2020:
            print(f"{i} * {j} = {i*j}")