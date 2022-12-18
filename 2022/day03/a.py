from collections import Counter

def get_priority(c):
    # a-z
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return (ord(c) - ord('a')) + 1

    # A-Z
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return (ord(c) - ord('A')) + 27

total_priority = 0

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        first_half = line[:len(line) // 2]
        second_half = line[len(line) // 2:]

        common_item_type = None
        first_half_count = Counter(first_half)
        for i in range(len(second_half)):
            if second_half[i] in first_half_count:
                common_item_type = second_half[i]

        total_priority += get_priority(common_item_type)

print(total_priority)