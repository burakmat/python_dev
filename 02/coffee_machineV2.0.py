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


def print_resources():
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${money}")
	pass


def check_resource(entry):
	for need in MENU[entry]["ingredients"]:
		if MENU[entry]["ingredients"][need] > resources[need]:
			print(f"{MENU[entry]['ingredients'][need]} and {resources[need]}")
			print(f"Sorry there is not enough {need}.")
			return False
	return True


def get_coin():
	total = 0
	coins = {"quarters": 0.25, "dimes": 0.1, "nickels": 0.05, "pennies": 0.01}
	print("Please insert coins.")
	for coin in coins:
		total += int(input(f"How many {coin}? ")) * coins[coin]
	return total


def make_coffee(coffee):
	for need in MENU[coffee]["ingredients"]:
		resources[need] -= MENU[coffee]["ingredients"][need]
	print(f"Here is your {coffee} ☕ Enjoy!")


resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
}
money = 0
while True:
	command = input("What would you like? (espresso/latte/cappuccino): ")

	if command == "off":
		break
	elif command == "report":
		print_resources()
		continue
	elif command == "espresso" or command == "latte" or command == "cappuccino":
		if not check_resource(command):
			continue
		change = get_coin() - MENU[command]["cost"]

		if change < 0:
			print(f"Sorry that's not enough money. Money refunded.")
			continue
		elif change > 0:
			print(f"Here is ${round(change, 2)} dollars in change.")
		money += MENU[command]["cost"]
		make_coffee(command)

