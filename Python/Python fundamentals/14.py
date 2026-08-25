#count vowels
def count_vowels(word):
    count=0

    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

count_vowels("python")

