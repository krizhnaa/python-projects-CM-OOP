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
        user_input = input(f'What would you like? ( {manu.get_items()} ) : ')


    can_mk = cm.is_resource_sufficient(manu.find_drink(user_input))

    # if can_mk == True:
    #     mm.make_payment()
    # print(mi.cost)



