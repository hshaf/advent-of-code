total_score = 0
plays = {"A": "X", "B": "Y", "C": "Z"}
points = {"A": 1, "B": 2, "C": 3}

with open('input.txt') as file:
    for line in file:
        round = line.split()
        # tie
        if plays[round[0]] == round[1]:
            total_score += points[round[0]] + 3
        
        # opp plays rock, you play paper (win)
        elif round[0] == "A" and round[1] == "Y":
            total_score += 2 + 6

        # opp plays rock, you play scissors (loss)
        elif round[0] == "A" and round[1] == "Z":
            total_score += 3

        # opp plays paper, you play rock (loss)
        elif round[0] == "B" and round[1] == "X":
            total_score += 1

        # opp plays paper, you play scissors (win)
        elif round[0] == "B" and round[1] == "Z":
            total_score += 3 + 6

        # opp plays scissors, you play rock (win)
        elif round[0] == "C" and round[1] == "X":
            total_score += 1 + 6

        # opp plays scissors, you play paper (loss)
        elif round[0] == "C" and round[1] == "Y":
            total_score += 2

print(total_score)