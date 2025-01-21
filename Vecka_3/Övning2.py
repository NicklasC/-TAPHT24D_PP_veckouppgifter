# 2.1a
answer = 0
for i in range(1, 11):
    answer += i
print("2a. Summan av talen 1 till 10 är: " + str(answer))


#2.1b
answer = 0
for i in range(1, 101):
    answer += i
print("2b. Summan av talen 1 till 100 är: " + str(answer))

#2.1C
#Pass



# 2.3a
filmer = [
    'Star Wars',
    'Inception',
    'The Matrix',
    'Blues brothers'
]

for film in filmer:
    print(film)

# 2.3b
filmer.append('Fellowship of the ring')

print("*"*5)

# 2.3c
filmer.insert(0,'The two towers')
for film in filmer:
    print(film)

# 2.3d
print(f"Fellowship of the ring har position: {filmer.index('Fellowship of the ring')}")
# 2.3e
filmer.remove('Inception')
print("Inception är borttagen. ")
print(f"Fellowship of the ring har nu position: {filmer.index('Fellowship of the ring')}")
#2.3f
print(f"Filmlistan har nu {len(filmer)} element.")

#2.3g
print("filmlistan i omvänd ordning blir: ")
for film in reversed(filmer):
    print(film)

#2.3h

print("filmlistan i sorterad ordning blir: ")
print(sorted(filmer))



