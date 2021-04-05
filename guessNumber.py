import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a Number between 1 and {x} >> '))
        if guess < random_number:
            print('Sorry ,Guess Again. Your Guess Number Is Low.')
        elif guess > random_number:
            print('Sorry ,Guess Again. Your Guess Number Is High.')

    print(f'Yay, Congraturations You Guessed The Number {random_number} Correctly')

guess(9)
