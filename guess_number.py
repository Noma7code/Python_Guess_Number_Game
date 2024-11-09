import random

name1 = input("Please input your name:\n")
name = name1.capitalize()  # ensures that the first letter of the name is capital


def guessing_power(guess_limit, number):  # function for the guessing game
    random_number = random.randint(1, number)
    try:
        while guess_limit > 0:
            guess = int(input('What is your guess for this round?\n'))
            guess_limit -= 1
            if random_number == guess:
                print("Congrats you got it right")
                break
            elif guess > number:
                print("oops no!!!,you guess is out of range\n")
                print(f"you have{guess_limit} guess(es)left\n")
            else:
                print("Sorry,that was not correct")
                print(f"you have {guess_limit} guess(es) left")
        print("Game over")
        print(f"The number was {random_number}")
    except ValueError:
        print("Only integers are allowed")


def easy():
    print(
        f" {name},I have a number in mind. Can you guess the number?"
        f" You have 5 chances to guess the right number\nHint: the number is between 1 and 20")
    guessing_power(5, 20)


def medium():
    print(
        f" {name},I have a number in mind,Can you guess the number. "
        f"You have 4 chances to guess the right number\nHint: the number is between 1 and 50")
    guessing_power(4, 50)


def hard():
    print(
        f" {name},I have a number in mind. Can you guess the number. "
        f"You have 2 chances to guess the right number\nHint: the number is between 1 and 100")
    guessing_power(2, 100)


# function to prompt the user to try again if the number of guess is exceeded
def try_again():
    again = input("Do you want to play again? Yes/No\n")
    if again.upper() == 'YES':
        welcome()
    elif again.upper() == 'NO':
        print("Thank you for playing")
    else:
        print("Wrong input")
        try_again()


def welcome():
    print(f"{name} welcome to the guessing game")
    difficulty = input("Input your level of difficulty: easy,medium or hard\n")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print("This is a wrong input")
        welcome()


# call of the welcome function to welcome the user before the game start
welcome()
