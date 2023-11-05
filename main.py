from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

manu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
# mi = MenuItem()

cm_continue = True

while cm_continue:
    user_input = input(f'What would you like? ( {manu.get_items()} ) : ')
    if user_input == 'off':
        cm_continue = False
    elif user_input == 'report':
        cm.report()
        mm.report()
    else:
        drink = manu.find_drink(user_input)
        if cm.is_resource_sufficient(drink):
            mm.make_payment(drink.cost)





