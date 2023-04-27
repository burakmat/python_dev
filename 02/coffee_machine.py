MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def resource_print():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml"
          f"\nCoffee: {resources['coffee']}g\nMoney: ${money}")


shut_down = False


def use_resource(coffee_in):
    coffee_needed = MENU[coffee_in]["ingredients"]["coffee"]
    water_needed = MENU[coffee_in]["ingredients"]["water"]
    if coffee_needed > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    elif water_needed > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    if coffee_in != "espresso":
        milk_needed = MENU[coffee_in]["ingredients"]["milk"]
        if milk_needed > resources["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        resources["milk"] -= milk_needed
    resources["water"] -= water_needed
    resources["coffee"] -= coffee_needed
    return True


def coin_process():
    coins = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}
    total = 0
    for key in coins:
        coin = int(input(f"How many {key}?"))
        total += coin * coins[key]
    return total


while not shut_down:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "off":
        shut_down = True
    elif coffee == "report":
        resource_print()
    elif use_resource(coffee):
        coin = coin_process()
        change = round(coin - MENU[coffee]["cost"], 2)
        if coin > MENU[coffee]["cost"]:
            resource_print()
            print(f"Here is ${change} in change.\nHere is your {coffee} ☕ Enjoy!")
        elif coin == MENU[coffee]["cost"]:
            resource_print()
            print("Here is your {coffee} ☕ Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")
