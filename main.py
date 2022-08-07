import random
n = random.randrange(1,10)
guess = int(input("enter the guess number:  "))
while n!= guess:
    if guess < n:
        print("too small")
        guess = int(input("enter the guess number again"))
    elif guess > n:
        print("too high")
        guess = int(input("enter the guess number again"))
    else:
        break
print("you guessed right ")
