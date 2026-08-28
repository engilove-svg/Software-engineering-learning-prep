text = input("Enter a sentence: ")

print("Characters:", len(text))
print("Words:", len(text.split()))
print("Spaces:",(text.count(" ")))

vowels=0
for char in text:
    if char.lower() in "aeiou":
        vowels += 1
print("Vowels:",vowels)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed:", text[::-1])

consonant=0
for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        consonant +=1
print("consonant:",consonant)