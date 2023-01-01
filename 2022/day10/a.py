instructions = []
register_values = dict()

with open('input.txt') as file:
    for line in file:
        instructions.append(line.strip("\n"))

cycle = 1
register_values[1] = 1
curr_reg_val = register_values[cycle]
for instruction in instructions:
    tokens = instruction.split()
    # 1 cycle
    if tokens[0] == "noop":
        cycle += 1

    # 2 cycles
    elif tokens[0] == "addx":
        cycle += 2
        register_values[cycle - 1] = curr_reg_val
        curr_reg_val += int(tokens[1])

    register_values[cycle] = curr_reg_val

ans = 0
cycles = [20, 60, 100, 140, 180, 220]
for c in cycles:
    ans += c * register_values[c]

print(ans)