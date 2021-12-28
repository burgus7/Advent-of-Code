print('DAY 2 PART 2')

commands = open('full_input_2', 'r')

depth = 0
horizontal = 0
aim = 0

for command in commands:
    cmd_splt = command.split()
    direction = cmd_splt[0]
    units = int(cmd_splt[1])

    if direction == "down":
        aim += units
    elif direction == "up":
        aim -= units
    elif direction == "forward":
        horizontal += units
        depth += aim * units

print (f"The answer is {depth*horizontal}")