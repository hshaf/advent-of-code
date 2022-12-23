grid = []

def search(x, y, dir, trees_seen, tree_height):
    if dir == "right":
        # skip
        stop_search = False
        if y + 1 > len(grid[x]) - 1:
            stop_search = True
        
        else:
            if grid[x][y + 1] < tree_height:
                trees_seen += 1
            
            else:
                stop_search = True
                trees_seen += 1

        if not stop_search:
            trees_seen = search(x, y + 1, dir, trees_seen, tree_height)

    elif dir == "left":
        # skip
        stop_search = False
        if y - 1 < 0:
            stop_search = True
        
        else:
            if grid[x][y - 1] < tree_height:
                trees_seen += 1

            else:
                stop_search = True
                trees_seen += 1

        if not stop_search:
            trees_seen = search(x, y - 1, dir, trees_seen, tree_height)

    elif dir == "down":
        # skip
        stop_search = False
        if x + 1 > len(grid) - 1:
            stop_search = True
        
        else:
            if grid[x + 1][y] < tree_height:
                trees_seen += 1

            else:
                stop_search = True
                trees_seen += 1

        if not stop_search:
            trees_seen = search(x + 1, y, dir, trees_seen, tree_height)

    elif dir == "up":
        # skip
        stop_search = False
        if x - 1 < 0:
            stop_search = True
        
        else:
            if grid[x - 1][y] < tree_height:
                trees_seen += 1

            else:
                stop_search = True
                trees_seen += 1

        if not stop_search:
            trees_seen = search(x - 1, y, dir, trees_seen, tree_height)

    return trees_seen

with open('input.txt') as file:
    for line in file:
        line = line.strip("\n")
        l = []
        for n in line:
            l.append(int(n))
        grid.append(l)

max_scenic_score = float('-inf')
for i in range(len(grid)):
    for j in range(len(grid[i])):
        max_scenic_score = max(max_scenic_score, (search(i, j, "left", 0, grid[i][j]) * search(i, j, "right", 0, grid[i][j]) * search(i, j, "down", 0, grid[i][j]) * search(i, j, "up", 0, grid[i][j])))

print(max_scenic_score)