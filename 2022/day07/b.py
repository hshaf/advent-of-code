from collections import Counter, deque

MAX_TOTAL_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
TARGET_UNUSED_SPACE = 30000000

class Directory:
    def __init__(self):
        self.size = 0
        self.files = []
        self.dir = []
        self.numSearches = 0

    def getSize(self):
        size = 0

        queue = deque([self])
        visited = set([self])

        while queue:
            v = queue.popleft()

            for file in v.files:
                size += file.size

            for w in v.dir:
                if w not in visited:
                    visited.add(w)
                    queue.append(w)

        self.size = size

        return self.size

class myFile:
    def __init__(self, name, size):
        self.size = size
        self.name = name

curr_path = ""
curr_dir = ""
d = dict()

with open('input.txt') as file:
    for line in file:
        line = line.strip("\n")
        tokens = line.split()
        # command
        if tokens[0] == "$":
            # change directory
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    curr_path = "/"
                    curr_dir = "/"
                
                elif tokens[2] == "..":
                    substring_idx = len(curr_path) - len(curr_dir)
                    curr_path = curr_path[:substring_idx]
                    curr_dir = curr_path.split("/")[-1]

                    count = Counter(curr_path)
                    if count["/"] > 1:
                        curr_dir = "/" + curr_dir

                else:
                    if curr_path == "/":
                        curr_path += tokens[2]
                        curr_dir = tokens[2]
                    
                    else:
                        curr_path += "/" + tokens[2]
                        curr_dir = "/" + tokens[2]
            
            # list files
            elif tokens[1] == "ls":
                if curr_path not in d:
                    d[curr_path] = Directory()
                    d[curr_path].numSearches += 1

        # output
        else:
            if d[curr_path].numSearches > 1:
                continue

            # directory
            if tokens[0] == "dir":
                dir_name = None
                if curr_path == "/":
                    dir_name = curr_path + tokens[1]
                else:
                    dir_name = curr_path + "/" + tokens[1]

                if dir_name not in d:
                    d[dir_name] = Directory()

                if d[dir_name] not in d[curr_path].dir:
                    d[curr_path].dir.append(d[dir_name])

            # file
            else:
                # check for duplicates
                for file in d[curr_path].files:
                    if tokens[1] == file.name:
                        continue

                f = myFile(tokens[1], int(tokens[0]))
                d[curr_path].files.append(f)

# update sizes for all directories
for key in d:
    d[key].getSize()

ans = float('inf')
used_space = d["/"].size
# find min size of directory that would free up enough space
for key in d:
    if TOTAL_DISK_SPACE - (used_space - d[key].size) >= TARGET_UNUSED_SPACE:
        ans = min(ans, d[key].size)

print(ans)