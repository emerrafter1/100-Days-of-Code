# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)


dictionary = {}
bid_again = True
highest_bid = 0
winner = ""

while bid_again == True:
    name = input("What is your name?")
    price = input("What is your bid?")


    dictionary[name] = price

    again = input("Are there others that need to bid? Y or N")

    if again == "N":
        bid_again = False

    for bidder in dictionary:

        bid_value = int(dictionary[bidder])

        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder

    print("\n" * 20)





print(f"The winner is {winner} with a bid £{highest_bid} ")

