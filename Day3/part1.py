gamma_string, epsilon_string = "", ""

with open("input1.txt", "r") as f:
    size = len(f.readline().rstrip())
    values = [int(line.rstrip(), 2) for line in f.readlines()]

for i in range(size):
    odd, even = 0, 0
    for j in range(len(values)):
        if values[j] % 2 == 0:
            even += 1
        else:
            odd += 1
        values[j] = values[j] >> 1
    if even > odd:
        gamma_string = f"0{gamma_string}"
        epsilon_string = f"1{epsilon_string}"
    else:
        gamma_string = f"1{gamma_string}"
        epsilon_string = f"0{epsilon_string}"

gamma, epsilon = int(gamma_string, 2), int(epsilon_string, 2)

print(gamma * epsilon)
