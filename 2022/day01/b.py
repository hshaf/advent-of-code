calories_list = []
calories = 0

with open('input.txt') as file:
    for line in file:
        if line.strip():
            calories += int(line.strip())

        else:
            calories_list.append(calories)
            calories = 0

calories_list.sort(reverse=True)
print(calories_list[0] + calories_list[1] + calories_list[2])