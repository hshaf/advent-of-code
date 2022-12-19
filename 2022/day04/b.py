ans = 0

with open('input.txt') as file:
    for line in file:
        pair = line.split(",")
        elf1 = pair[0].split("-")
        elf2 = pair[1].split("-")

        if (int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[0])) or (int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[1])):
            ans += 1

        elif (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[0])) or (int(elf2[0]) <= int(elf1[1]) and int(elf2[1]) >= int(elf1[1])):
            ans += 1

print(ans)