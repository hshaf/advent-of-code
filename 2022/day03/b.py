from collections import Counter

def get_priority(c):
    # a-z
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return (ord(c) - ord('a')) + 1

    # A-Z
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return (ord(c) - ord('A')) + 27

total_priority = 0
lines = []

with open('input.txt') as file:
    for line in file:
        lines.append(line.strip())

i = 2
common_item_type = None
while i < len(lines):
    first_line_count = Counter(lines[i - 2])
    second_line_count = Counter(lines[i - 1])
    for j in range(len(lines[i])):
        if lines[i][j] in first_line_count and lines[i][j] in second_line_count:
            common_item_type = lines[i][j]

    total_priority += get_priority(common_item_type)
    i += 3

print(total_priority)