hor, ver, aim = (
    0,
    0,
    0,
)

with open("input.txt", "r") as f:
    commands = [line.rstrip() for line in f.readlines()]

for x in commands:
    direction, value = x.split(" ")
    value = int(value)
    if direction == "forward":
        hor += value
        ver += aim * value
    elif direction == "down":
        aim += value
    else:
        aim -= value

print(ver * hor)
