depths, count = [], 0

with open("input.txt", "r") as f:
    depths = [int(line.rstrip()) for line in f.readlines()]

for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        count += 1

print(count)
