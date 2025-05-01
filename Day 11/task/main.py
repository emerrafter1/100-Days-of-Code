import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards = [random.choice(cards)]
print(f"Dealer's first card: {dealer_cards}")

user_cards = [random.choice(cards)]
print(f"Your first card: {user_cards}")

dealer_cards.append(random.choice(cards))
print("Dealer has taken another card from the deck")

user_cards.append(random.choice(cards))
print(f"You have chosen a second card: {user_cards}")

user_has_lost = False

while sum(dealer_cards) < 17:
    dealer_cards.append(random.choice(cards))
    print("Dealer has taken another card from the deck...")

    while sum(dealer_cards) > 21 and 11 in dealer_cards:
        index_of_ace = dealer_cards.index(11)
        dealer_cards[index_of_ace] = 1



def pick_another_card():
    global user_has_lost

    if sum(user_cards) > 21:

        while 11 in user_cards:
            index_of_ace = user_cards.index(11)
            user_cards[index_of_ace] = 1
        else:
            user_has_lost = True

    else:
        another_card = input("Do you want to take another card?")
        if another_card == "Y":
            user_cards.append(random.choice(cards))
            print(user_cards)
            pick_another_card()



pick_another_card()



print(f"Dealer's cards: {dealer_cards}")
print(f"Your cards: {user_cards}")



if user_has_lost:
    print("Dealer wins the game")
elif sum(dealer_cards) > 21 or sum(user_cards) > sum(dealer_cards):
    print("You win!")
elif sum(user_cards) == sum(dealer_cards):
    print("It's a draw!")
else:
    print("Dealer wins the game")






