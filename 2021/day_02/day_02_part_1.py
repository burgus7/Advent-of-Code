print('DAY 2 PART 1')

commands = open('full_input_2', 'r')

depth = 0
horizontal = 0

for command in commands:
    cmd_splt = command.split()
    direction = cmd_splt[0]
    units = int(cmd_splt[1])

    if direction == "forward":
        horizontal += units
    elif direction == "down":
        depth += units
    else:
        depth -= units


print (f"The answer is {depth*horizontal}")