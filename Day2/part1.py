hor, ver, commands = 0, 0, []

with open("input.txt", "r") as f:
    commands = [line.rstrip() for line in f.readlines()]

for x in commands:
    direction, value = x.split(" ")
    value = int(value)
    if direction == "forward":
        hor += value
    elif direction == "down":
        ver += value
    else:
        ver -= value

print(ver * hor)
