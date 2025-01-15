print("The match is over, lets see the results!")
tottenham_goals = int(input("How many goals did Tottenham score? "))
liverpool_goals = int(input("How many goals did Liverpool score? "))

if tottenham_goals > liverpool_goals:
    print("Tottenham won the match!")
    print(f"Tottenham won by {tottenham_goals - liverpool_goals} goals")
elif tottenham_goals < liverpool_goals:
    print("Liverpool won the match!")
    print(f"Liverpool won by {liverpool_goals - tottenham_goals} goals")
else:
    print("It was a draw!")