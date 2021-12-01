depths, count = [], 0

with open("input.txt", "r") as f:
    depths = [int(line.rstrip()) for line in f.readlines()]

for i in range(1, len(depths) - 2):
    three_sum = sum([depths[i - 1], depths[i], depths[i + 1]])
    three_sum_next = sum([depths[i], depths[i + 1], depths[i + 2]])
    if three_sum_next > three_sum:
        count += 1


print(count)
