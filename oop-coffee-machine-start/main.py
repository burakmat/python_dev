from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffee=CoffeeMaker()
money_machine=MoneyMachine()

while 1:
    print(menu.get_items())
    choice=input("What would you like? :")
    if choice=="off":
        break
    elif choice=="report":
        coffee.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if not coffee.is_resource_sufficient(drink):
            break
        else:
            if money_machine.make_payment(drink.cost):
                coffee.make_coffee(drink)
