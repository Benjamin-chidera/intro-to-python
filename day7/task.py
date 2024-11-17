# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

data = {}
continue_bid = True


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]

        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while continue_bid:
    print("Welcome to the secret auction program.")
    user_name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: $"))

    # data["name"] = user_name
    # data["bid"] = user_bid

    data[user_name] = user_bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        continue_bid = False
        find_highest_bidder(data)
    else:
        print("\n" * 1)


# highest_bidder = max(data, key=data.get)
# highest_bid = data[highest_bidder]
# print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
