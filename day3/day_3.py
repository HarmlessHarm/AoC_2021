import numpy as np


summed = np.zeros(12)
print(summed)


with open('day3/input_3.txt', 'r') as file:

    lines = file.readlines()
    NoL = len(lines)
    all_bits = list()
    for line in lines:
        bits = np.array(list(map(int, list(line.strip()))))
        all_bits.append(bits)

        summed += bits
    all_bits = np.array(all_bits)
    
gamma_rate = int("".join(map(str, map(int, summed >= 500))), 2)
epsilon_rate = int("".join(map(str, map(int, summed < 500))), 2)

print(f"===")
print(f"Part 1")
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate}")
print(f"Power consumtion: {gamma_rate * epsilon_rate}")


oxigen_bits = all_bits.copy()
carbon_bits = all_bits.copy()

for i in range(all_bits.shape[1]):
    
    if (oxigen_bits.shape[0] > 1):
        oxigen_column_sum = np.sum(oxigen_bits[:,i])
        oxigen_sign_bit = oxigen_column_sum >= (oxigen_bits.shape[0] / 2)
        oxigen_bits = oxigen_bits[oxigen_bits[:,i] == oxigen_sign_bit]

    if (carbon_bits.shape[0] > 1):
        carbon_column_sum = np.sum(carbon_bits[:,i])
        carbon_sign_bit = carbon_column_sum < (carbon_bits.shape[0] / 2)
        carbon_bits = carbon_bits[carbon_bits[:,i] == carbon_sign_bit]
    
oxigen_rate = int("".join(list(map(str, oxigen_bits[0]))),2)
carbon_rate = int("".join(list(map(str, carbon_bits[0]))),2)

print(f"===")
print(f"Part 2")
print(f"Oxigen rate: {oxigen_rate}")
print(f"Carbon rate: {carbon_rate}")
print(f"Life support rating: {oxigen_rate * carbon_rate}")