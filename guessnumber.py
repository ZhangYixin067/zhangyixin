import random
def get_secret_number():
    return random.randint(1, 100)
secret= get_secret_number()
def get_guess():
    guess=int(input("Guess a number between 1 and 100: "))
    return guess
def check_guess(secret, guess):
    if secret == guess:
        return True
    else:
        return False
while True:
    guess=get_guess()
    if check_guess(secret, guess):
        print("True")
        break
    else:
        print("False")