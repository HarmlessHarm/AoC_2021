import numpy as np


summed = np.zeros(12)
print(summed)


with open('day3/input_3.txt', 'r') as file:

    lines = file.readlines()
    NoL = len(lines)
    for line in lines:
        bits = np.array(list(map(int, list(line.strip()))))

        summed += bits
    

gamma_rate = int("".join(map(str, map(int, summed >= 500))), 2)
epsilon_rate = int("".join(map(str, map(int, summed < 500))), 2)

print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumtion: {gamma_rate * epsilon_rate}")


