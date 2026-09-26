from res import MENU, resources

WATER = "water"
MILK = "milk"
COFFEE = "coffee"
res_names = [WATER, MILK, COFFEE]
COINS = [25, 10, 5, 1]
total_profit = 0


def print_report():
    print(
        f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml , \nCoffee: {resources['coffee']} g, \nMoney: ${total_profit}"
    )


def get_missing_res(drink_name):
    res_needed = MENU[drink_name]["ingredients"]
    missing_res = []
    for res_name in res_names:
        if resources[res_name] < res_needed[res_name]:
            missing_res.append(res_name)
    return missing_res


def calculate_total_amount(inserted_nr_coins):
    amount = 0
    for i in range(0, len(COINS) - 1):
        amount += COINS[i] * inserted_nr_coins[i]
    return amount


def calculate_change(total_amount_inserted, chosen_drink_cost):
    return total_amount_inserted - chosen_drink_cost


def format_cents(cents):
    return f"$ {cents / 100}"


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "off":
        break
    elif user_choice == "report":
        print_report()
        continue
    missing_res = get_missing_res(user_choice)
    if len(missing_res) != 0:
        print(f"Sorry there is not enough {', '.join(missing_res)}")
    print("Please insert coins.")
    inserted_nr_coins = []
    inserted_nr_coins.append(int(input("How many quarters?")))
    inserted_nr_coins.append(int(input("How many dimes?")))
    inserted_nr_coins.append(int(input("How many nickles?")))
    inserted_nr_coins.append(int(input("How many pennies?")))
    total_amount_inserted = calculate_total_amount(inserted_nr_coins)
    chosen_drink_cost = MENU[user_choice]["cost"]
    if total_amount_inserted < chosen_drink_cost:
        print(f"Sorry that's not enough money. Money refunded.")
    elif total_amount_inserted > chosen_drink_cost:
        change = calculate_change(total_amount_inserted, chosen_drink_cost)
        print(f"Here is your change {format_cents(change)}")
        total_profit += total_amount_inserted - change
    else:
        total_profit += total_amount_inserted
    print(f"Here is your {user_choice} Enjoy!")
