from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

manu = Menu()

cm_continue = True

while cm_continue:
    user_input = input(f'What would you like? ( {manu.get_items()} ) : ')
    if user_input == 