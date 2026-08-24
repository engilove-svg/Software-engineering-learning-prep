



import random
words=["apple","banana","grapes","strawberry","orange","papaya"]
word=random.choice(words)
print(word)
guessed_letters=[]
while True:
   guess=input("Guess a letter: ")

   for letter in word:
      if letter==guess:
         print(letter,end="")
      else:
         print("_",end="")

   print()