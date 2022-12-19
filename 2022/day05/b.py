NUM_STACKS = 0

stacks = None
run_parser = True

def is_alpha(c):
    return ord('A') <= ord(c) and ord('Z') >= ord(c)

with open('input.txt') as file:
    for line in file:
        # parse stacks
        if run_parser:
            if not line.strip():
                run_parser = False
                # reverse order of each stack
                for i in range(NUM_STACKS):
                    stacks[i].reverse()
                continue

            if NUM_STACKS == 0:
                NUM_STACKS = (len(line) + 1) // 4
                stacks = [[] for _ in range(NUM_STACKS)]

            # add crates to stacks
            i, j = 0, 1
            while j < len(line):
                if is_alpha(line[j]):
                    stacks[i].append(line[j])
                i += 1
                j += 4
        
        # perform move operations
        else:
            operation = line.strip("\n").split()
            num_crates = int(operation[1])
            src_stack = int(operation[3]) - 1
            dst_stack = int(operation[5]) - 1

            crates = []
            for _ in range(num_crates):
                crates.append(stacks[src_stack].pop())
            
            crates.reverse()
            stacks[dst_stack].extend(crates)

for i in range(NUM_STACKS):
    print(stacks[i][-1], end="")

print()
