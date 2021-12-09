
# Day 2.1

commands = {
    'forward': 0,
    'down': 0,
    'up': 0
}

with open("day2/input_2.txt", 'r') as file:

    for line in file.readlines():
        cmd, N = line.split(' ')
        
        commands[cmd] += int(N)

x = commands['forward']
y = commands['down'] - commands['up']


print(f"Final position is {x}, {y}, multiplied: {x * y}")


# Day 2.2

position = 0
depth = 0
aim = 0

with open("day2/input_2.txt", 'r') as file:

    for line in file.readlines():
        cmd, N = line.split(' ')
        N = int(N)
        if cmd == 'down':
            aim += N
        elif cmd == 'up':
            aim -= N

        elif cmd == 'forward':
            position += N
            depth += N * aim

print(f"Final position is {position}, {depth}, multiplied: {position * depth}")