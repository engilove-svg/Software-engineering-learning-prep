#NUMBER GUESSING GAME VERSION 1

secret_code = 4
attempts = 0

while attempts < 5:
    guess=int(input("Enter a guess: "))
    attempts += 1

    if guess == secret_code:
        print("CORRECT!")
        break

    elif guess > secret_code:
        print("TOO HIGH!")
    else:
        print("TOO LOW!")

if guess != secret_code :
    print("GAME OVER!")
    print(f"The number was {secret_code}.")
