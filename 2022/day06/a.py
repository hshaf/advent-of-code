buffer = None

with open('input.txt') as file:
    for line in file:
        buffer = line.strip()

char_count = 4
# use a sliding window of size 4
for i in range(3, len(buffer)):
    char1 = buffer[i - 3]
    char2 = buffer[i - 2]
    char3 = buffer[i - 1]
    char4 = buffer[i]

    if char1 != char2 and char1 != char3 and char1 != char4 and char2 != char3 and char2 != char4 and char3 != char4:
        break

    char_count += 1

print(char_count)