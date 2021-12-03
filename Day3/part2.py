with open("input1.txt", "r") as f:
    values = [line.rstrip() for line in f.readlines()]


def filterOxygen(oxygen: list, even: int, odd: int, pos: int) -> None:
    delete_vals = []
    if even > odd:
        for x in oxygen:
            if x[pos] != "0":
                delete_vals.append(x)
    else:
        for x in oxygen:
            if x[pos] != "1":
                delete_vals.append(x)

    for val in delete_vals:
        oxygen.remove(val)


def filterC02(c02: list, even: int, odd: int, pos: int) -> None:
    delete_vals = []
    if even > odd:
        for x in c02:
            if x[pos] != "1":
                delete_vals.append(x)
    else:
        for x in c02:
            if x[pos] != "0":
                delete_vals.append(x)

    for val in delete_vals:
        c02.remove(val)


oxygen, c02, i, j = [*values], [*values], 0, 0

while len(oxygen) > 1:
    odd, even = 0, 0
    for x in oxygen:
        if x[i] == "0":
            even += 1
        else:
            odd += 1
    filterOxygen(oxygen, even, odd, i)
    i += 1

while len(c02) > 1:
    odd, even = 0, 0
    for x in c02:
        if x[j] == "0":
            even += 1
        else:
            odd += 1
    filterC02(c02, even, odd, j)
    j += 1

oxygen_decimal, c02_decimal = int(oxygen[0], 2), int(c02[0], 2)
print(oxygen_decimal, c02_decimal)
print(oxygen_decimal * c02_decimal)
