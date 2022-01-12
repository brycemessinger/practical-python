import random
# random_num = random.randint(1,100)
random_num = 71

name = str(input("Howdy, what's your name?\n"))
attempts = 1

print(name, " I'm thinking of a number between 1 and 100.")
number_guess = int(input("Try to guess my number.\n"))
def number_game():
    print("Your guess?", number_guess)
    if number_guess > random_num:
        attempts + 1
        # too_high()
        print(attempts)
    elif number_guess < random_num:
        attempts + 1
        print("attempts")
        # too_low()4
    elif number_guess == random_num:
        print("Well done,", name, "You found my number in", attempts, "attempts!")

# def too_low():
#      str(input("Your guess is too low! Try again."))
#      number_game()
# def too_high():
#     str(input("Your guess is too high! Try again."))
#     number_game()