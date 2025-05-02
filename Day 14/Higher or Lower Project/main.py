import random

import game_data

game_data = game_data.data






# Make sure we don't compare the same person



def guess_followers():
    person_a = random.choice(game_data)
    score = 0


    gameOver = False

    while gameOver == False:
        followers_a = person_a["follower_count"]

        person_b = random.choice(game_data)
        while person_b == person_a:
            person_b = random.choice(game_data)

        followers_b = person_b["follower_count"]

        guess = input(f"""
        Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}.
        Against B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}.
        Who has more followers? Type 'A' or 'B':
        """)

        if followers_a > followers_b and guess == "A":
            score += 1
            print(f"You are correct, {person_a['name']} has more followers! Let's play again.Score is {score}")


        elif followers_a < followers_b and guess == "B":
            score += 1
            print(f"You are correct, {person_b['name']} has more followers! Let's play again.\nScore is {score}")
            person_a = person_b



        elif followers_a == followers_b:
            print(f"They have the same followers! Let's play again.")
        elif followers_a < followers_b and guess == "A":
            gameOver = True
            print(f"Incorrect {person_b['name']} has more followers. Game over!\nScore was {score}")
        else :
            gameOver = True
            print(f"Incorrect {person_a['name']} has more followers. Game over!\nScore was {score}")


guess_followers()


