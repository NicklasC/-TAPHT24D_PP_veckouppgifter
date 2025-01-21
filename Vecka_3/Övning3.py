# Kvittouträknaren

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

#### Version 2:
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

print(f"Det blir {sum} kr totalt, alltså {(sum / number_of_persons):.2f} kr per person. Välkommen åter!")
