
# Day 1 read input
with open("./day1/input_1.txt", 'r') as file:

    depths = list(map(int, file.readlines()))


prev_depth = float('inf')
increase_cnt = 0
for depth in depths:

    if depth > prev_depth:
        increase_cnt += 1
    
    prev_depth = depth

print(f"Depth increases: {increase_cnt}")

prev_sum = float('inf')
increase_cnt = 0

for i in range(len(depths) - 2):
    summed = sum(depths[i:i+3])

    if summed > prev_sum:
        increase_cnt += 1

    prev_sum = summed

print(f"Summed depth increse: {increase_cnt}")