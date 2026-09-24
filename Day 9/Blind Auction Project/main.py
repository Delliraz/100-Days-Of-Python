# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

dict = {}

while True:
    name = input("What is your name?")
    price = int(input("What is your price?"))
    dict[name]=price
    is_over = input("Are there other bids? yes/no")
    if is_over == "no":
        break
    print("\n" * 20)

max_bid = 0
max_bid_name = ""
for key in dict:
    if dict[key] > max_bid:
        max_bid= dict[key]
        max_bid_name = key

print(f"Aaaand the winner is {max_bid_name}")