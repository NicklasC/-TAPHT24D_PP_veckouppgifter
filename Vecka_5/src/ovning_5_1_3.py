def count_vowels(word):
    count=0
    for letter in word:
        if letter in "aeiouy":
            count+=1
    return count
