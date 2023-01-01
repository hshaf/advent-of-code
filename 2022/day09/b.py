from collections import deque


GRID_SIZE = 300
NUM_KNOTS = 10
HEAD_IDX = 0

grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# track positions visited by the tail at least once
visited = set()
op = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

# start T and H in middle of the grid
start_x = len(grid) // 2
start_y = len(grid[0]) // 2
knots = [[start_x, start_y] for _ in range(NUM_KNOTS)]

grid[start_x][start_y] = "#"

visited.add((start_x, start_y))

def move_knot(new_x, new_y):
    grid[new_x][new_y] = "#"
    if (new_x, new_y) not in visited:
        visited.add((new_x, new_y))

def get_sign(num):
    if num == 0:
        return 0

    return -1 if num < 0 else 1

with open('input.txt') as file:
    for line in file:
        line = line.strip("\n")
        tokens = line.split()
        
        i = 0
        while i < int(tokens[1]):
            # move head
            knots[HEAD_IDX][0] += op[tokens[0]][0]
            knots[HEAD_IDX][1] += op[tokens[0]][1]

            # check if remaining knots need to be moved
            update_knots = False
            dx = knots[HEAD_IDX][0] - knots[1][0]
            dy = knots[HEAD_IDX][1] - knots[1][1]
            if abs(dx) > 1 or abs(dy) > 1:
                knots[1][0] += get_sign(dx)
                knots[1][1] += get_sign(dy)
                update_knots = True
            
            if update_knots:
                for j in range(2, NUM_KNOTS):
                    dx = knots[j - 1][0] - knots[j][0]
                    dy = knots[j - 1][1] - knots[j][1]
                    if abs(dx) > 1 or abs(dy) > 1:
                        knots[j][0] += get_sign(dx)
                        knots[j][1] += get_sign(dy)

            move_knot(knots[-1][0], knots[-1][1])

            i += 1


print(len(visited))
# print(visited)
# print grid
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         print(grid[i][j], end="")
#     print()