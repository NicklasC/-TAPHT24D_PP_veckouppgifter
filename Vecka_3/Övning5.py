import random


def print_om_det_bränns(tal,guess):
    if abs(guess - tal) <= 5:
        print("Nu börjar det börjar brännas!")


tal = random.randint(1, 100)

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

while True:
    try:
        guess = int(input("Gissa:"))
    except ValueError:
        print("Du kan endast gissa ett heltal mellan 1 och 100")
        continue

    if  1 <= guess <= 100:
        if guess < tal:
            print("Nej, det är för lågt!")
            print_om_det_bränns(tal,guess)
        elif guess > tal:
            print("Nej, det är för högt!")
            print_om_det_bränns(tal,guess)
        else:
            print("Du gissade rätt!")
            break
    else:
        print("Din gissning måste vara mellan 1 och 100, försök igen...")

