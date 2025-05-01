import random

def guess_number_game():



    number = random.randint(1, 100)

    difficulty = input("Choose difficulty. Type easy or hard: ")

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:

        guess = int(input("Guess a number"))

        if guess > number:
            print("Too high")
            attempts -= 1

        elif guess < number:
            print("Too low")
            attempts -= 1

        else:
            return f"Correct, you guess the number correctly, it was {number}"

    return f"You failed to guess the correct number, it was {number}"


print(guess_number_game())

