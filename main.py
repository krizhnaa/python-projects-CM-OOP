from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

manu = Menu()
cm = CoffeeMaker()

cm_continue = True

while cm_continue:
    user_input = input(f'What would you like? ( {manu.get_items()} ) : ')
    if user_input == 'off':
        cm_continue = False

    if user_input == 'report':
        print(cm.report())
        user_input = input(f'What would you like? ( {manu.get_items()} ) : ')

    if cm.is_resource_sufficient(manu.find_drink(user_input)) == True:
        print('can make')
    else:
        print('Sorry')
