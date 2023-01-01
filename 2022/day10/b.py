CRT_HEIGHT = 6
CRT_WIDTH = 40

instructions = []
register_values = dict()
crt = [["." for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)]

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

curr_reg_val = 1
crt_pxl_0 = 0
crt_pxl_1 = 1
crt_pxl_2 = 2
for i in range(CRT_HEIGHT):
    for j in range(CRT_WIDTH):
        reg_val = register_values[(j + 1) + (i * 40)]
        if curr_reg_val != reg_val:
            crt_pxl_0 += reg_val - curr_reg_val
            crt_pxl_1 += reg_val - curr_reg_val
            crt_pxl_2 += reg_val - curr_reg_val
            curr_reg_val = reg_val
        
        # draw
        if j == crt_pxl_0 or j == crt_pxl_1 or j == crt_pxl_2:
            crt[i][j] = "#"

for i in range(CRT_HEIGHT):
    for j in range(CRT_WIDTH):
        print(crt[i][j], end="")
    print()