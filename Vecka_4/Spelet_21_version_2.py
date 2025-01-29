import random
sum = 0
tal = 1
card = random.randint(1, 13)
while True:
    sum += tal
    if sum > card:
        break
    else:
        tal += 1
print(tal)

