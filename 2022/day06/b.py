from collections import Counter
buffer = None

with open('input.txt') as file:
    for line in file:
        buffer = line.strip()

char_count = 14
# use a sliding window of size 14
for i in range(13, len(buffer)):
    s = buffer[i - 13:i + 1]
    c = Counter(s)
    is_unique = True
    for k in c:
        if c[k] > 1:
            is_unique = False

    if is_unique:
        break

    char_count += 1

print(char_count)