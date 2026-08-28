# ---Challenge: Palindrome Checker------

text=input("Enter a word: ")
original=text.lower()
reverse=text[::-1]

if original==reverse:
    print("It is a palindrome.")
else:
    print("Not palindrome.")

