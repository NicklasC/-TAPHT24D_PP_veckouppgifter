# a
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)


# b
print("")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
# c
print("")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or x == 4 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)

# d
print("")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3:
            s += "#"
        elif y == 3:
            s += "#"
        else:
            s += "."
    print(s)