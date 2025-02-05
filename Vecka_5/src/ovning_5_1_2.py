# Returnerar summan av alla tal i listan
def sum_list(list):
    sum = 0
    for item in list:

        sum += item
    if sum == 0:
        return None
    else:
        return sum
