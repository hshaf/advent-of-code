total_score = 0

with open('input.txt') as file:
    for line in file:
        round = line.split()
        # lose
        if round[1] == "X":
            if round[0] == "A":
                total_score += 3
            elif round[0] == "B":
                total_score += 1
            elif round[0] == "C":
                total_score += 2
        # draw
        elif round[1] == "Y":
            if round[0] == "A":
                total_score += 1 + 3
            elif round[0] == "B":
                total_score += 2 + 3
            elif round[0] == "C":
                total_score += 3 + 3
        # win
        elif round[1] == "Z":
            if round[0] == "A":
                total_score += 2 + 6
            elif round[0] == "B":
                total_score += 3 + 6
            elif round[0] == "C":
                total_score += 1 + 6

print(total_score)