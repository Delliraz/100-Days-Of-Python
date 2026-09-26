import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


def print_both():
    print("User cards:")
    print(user_cards)
    print("PC cards:")
    print(computer_cards)


def define_winner():
    user_sum = sum(user_cards)
    pc_sum = sum(computer_cards)

    if user_sum > 21:
        print("PC wins, user > 21")
        return
    user_sum -= 21
    pc_sum -= 21
    if user_sum > pc_sum:
        print("User wins")
    else:
        print("PC wins")


def put_random_card(l, nr_cards):
    for i in range(0, nr_cards):
        l.append(random.choice(cards))


put_random_card(user_cards, 2)
put_random_card(computer_cards, 1)

print_both()

want_continue = input("You want to continue y/n?")

if want_continue == "y":
    put_random_card(user_cards, 1)
    put_random_card(computer_cards, 1)
    print_both()
    define_winner()
else:
    put_random_card(computer_cards, 1)
    print_both()
    define_winner()
