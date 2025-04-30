import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options = [rock, paper, scissors]

computer_choice = random.choice(options)

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:"))

if 0 <= user_input <= 2:
    user_choice = options[user_input]
    print(f"You chose:\n" + user_choice)
    print(f"Computer chose:\n" + computer_choice)
    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == rock and computer_choice == scissors) or (user_choice == paper and computer_choice == rock) or (user_choice == scissors and computer_choice == paper):
        print("You win!")
    else:
        print("Computer wins :(")

else:
    print("Invalid input")



