from collections import deque


GRID_SIZE = 300

grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
# track positions visited by the tail at least once
visited = set()
op = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

# start T and H in middle of the grid
h_x = len(grid) // 2
h_y = len(grid[h_x]) // 2
t_x = h_x
t_y = h_y

grid[h_x][h_y] = "#"

visited.add((t_x, t_y))

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
            h_x += op[tokens[0]][0]
            h_y += op[tokens[0]][1]

            # check if tail needs to be moved
            dx = h_x - t_x
            dy = h_y - t_y
            if abs(dx) > 1 or abs(dy) > 1:
                t_x += get_sign(dx)
                t_y += get_sign(dy)
                if (t_x, t_y) not in visited:
                    move_knot(t_x, t_y)

            i += 1


print(len(visited))
# print(visited)
# print grid
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         print(grid[i][j], end="")
#     print()