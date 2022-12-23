grid = []
ans = []

def search(x, y, dir, max_height_seen):
    if dir == "right":
        # skip
        if y - 1 < 0:
            if (x, y) not in ans:
                ans.append((x, y))
        
        else:
            if grid[x][y - 1] < grid[x][y] and grid[x][y] > max_height_seen:
                if (x, y) not in ans:
                    ans.append((x, y))
            
            max_height_seen = max(max_height_seen, grid[x][y - 1])

        if y + 1 < len(grid[x]):
            search(x, y + 1, dir, max_height_seen)

    elif dir == "left":
        # skip
        if y + 1 > len(grid[x]) - 1:
            if (x, y) not in ans:
                ans.append((x, y))
        
        else:
            if grid[x][y + 1] < grid[x][y] and grid[x][y] > max_height_seen:
                if (x, y) not in ans:
                    ans.append((x, y))

            max_height_seen = max(max_height_seen, grid[x][y + 1])

        if y - 1 >= 0:
            search(x, y - 1, dir, max_height_seen)

    elif dir == "down":
        # skip
        if x - 1 < 0:
            if (x, y) not in ans:
                ans.append((x, y))
        
        else:
            if grid[x - 1][y] < grid[x][y] and grid[x][y] > max_height_seen:
                if (x, y) not in ans:
                    ans.append((x, y))

            max_height_seen = max(max_height_seen, grid[x - 1][y])

        if x + 1 < len(grid):
            search(x + 1, y, dir, max_height_seen)

    elif dir == "up":
        # skip
        if x + 1 > len(grid) - 1:
            if (x, y) not in ans:
                ans.append((x, y))
        
        else:
            if grid[x + 1][y] < grid[x][y] and grid[x][y] > max_height_seen:
                if (x, y) not in ans:
                    ans.append((x, y))

            max_height_seen = max(max_height_seen, grid[x + 1][y])

        if x - 1 >= 0:
            search(x - 1, y, dir, max_height_seen)

with open('input.txt') as file:
    for line in file:
        line = line.strip("\n")
        l = []
        for n in line:
            l.append(int(n))
        grid.append(l)

# start from left, sweep to right
for i in range(len(grid)):
    search(i, 0, "right", -1)
    search(i, len(grid[i]) - 1, "left", -1)

for i in range(len(grid[0])):
    search(0, i, "down", -1)
    search(len(grid) - 1, i, "up", -1)

print(len(ans))