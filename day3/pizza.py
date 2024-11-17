print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M, or L: ")
want_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


price = 0

if pizza_size == "S":
    price += 15
elif pizza_size == "M":
    price += 20
elif pizza_size == "L":
    price += 25

    if want_pepperoni == "Y":
        price += 2

    if extra_cheese == "Y":
        price += 1

else:
    print("Invalid input. Please enter S, M, or L.")


print(f"Your final bill is: ${price}.")
