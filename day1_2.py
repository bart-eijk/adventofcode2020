numbers = [int(line.strip()) for line in open('day1_input.txt')]
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(f"{i} * {j} * {k} = {i*j*k}")