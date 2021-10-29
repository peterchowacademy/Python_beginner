import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Please guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"you guess number is too low, try again! ")
        elif guess > random_number:
            print(f"you guess number if too high, try again!")
        else:
            print(f"yay, you got the number {random_number} correctly ")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(1,x)
        else: 
            guess = low #can be either low or high, which equals to the guess number
        feedback = input(f"is {guess} too high (H) or too low (L) or correct? (C)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else: 
            print(f"yay, the computer guess right on your number {guess} !")

guess(100)
# computer_guess(100)