max_calories = float('-inf')
calories = 0

with open('input.txt') as file:
    for line in file:
        if line.strip():
            calories += int(line.strip())

        else:
            max_calories = max(max_calories, calories)
            calories = 0

print(max_calories)