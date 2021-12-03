music = 0
world = 0

strings = []

with open('day1/input_1.txt', 'r') as f:
    for metal in f.readlines():
        metal = int(metal)
        if metal > music:
            world += 1
            strings.append("1")
        else:
            strings.append("-1")
        
        music = metal

print(world - 1)

print(strings)
