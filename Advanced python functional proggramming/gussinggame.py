answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("well done, tou guessed it")
    else:
        print("print guess lower")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done, tou guessed it")
else:
    print("Sorry, you have not guessed")
