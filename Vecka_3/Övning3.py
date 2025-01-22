# Kvittouträknaren
# Enabla den version du vill testa, disabla de andra raderna

### Version 1:
# sum = 0
# while True:
#     usr_input = input("Skriv in ett belopp:")
#     if usr_input == "quit" or usr_input == "avsluta":
#         break
#     try:
#         number = int(usr_input)
#         sum += number
#     except ValueError:
#         print("Endast heltal är tillåtna, försök igen...")
# print(f"Det blir totalt {sum} kr. Välkommen åter!")

# #### Version 2:
# sum = 0
# while True:
#     usr_input = input("Skriv in ett belopp:")
#     if usr_input == "quit" or usr_input == "avsluta":
#         break
#     try:
#         number = int(usr_input)
#         sum += number
#     except ValueError:
#         print("Endast heltal är tillåtna, försök igen...")
#
# while True:
#     usr_input = input("Hur många är ni?")
#     try:
#         number_of_persons = int(usr_input)
#         break
#     except ValueError:
#         print("Endast heltal är tillåtna, försök igen...")
#
# print(f"Det blir {sum} kr totalt, alltså {(sum / number_of_persons):.2f} kr per person. Välkommen åter!")

#### Version 3:
sum = 0
while True:
    usr_input = input("Skriv in ett belopp:")
    if usr_input == "quit" or usr_input == "avsluta":
        break
    try:
        number = int(usr_input)
        sum += number
    except ValueError:
        print("Endast heltal är tillåtna, försök igen...")

while True:
    usr_input = input("Hur många är ni?")
    try:
        number_of_persons = int(usr_input)
        break
    except ValueError:
        print("Endast heltal är tillåtna, försök igen...")

while True:
    usr_input = input("Hur mycket dricks vill du ge? 10% är standard: ")
    try:
        if usr_input == "":
            tip = 10
            break
        tip = int(usr_input)
        if 0 <= tip <= 100:
            break
        else:
            raise ValueError
    except ValueError:
        print("Ange procent mellan 0 och 100, försök igen...")
print(f"Det blir {sum} kr totalt + {tip}% dricks. Det blir totalt {(sum / number_of_persons)* (1 + tip / 100):.2f} kr per person. Välkommen åter!")
