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
    "money":0,
}
# TODO:Print report on available resources.
def update_resources():
    pass

def resource_report():

    print("===============")
    print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:${resources['money']}")
    print("===============\n")




# TODO:Take User input on what kind of coffee user need.

def user_choice(user_choice):
    pass





# TODO:Check resources whether sufficient or not.

def check_resources(coffee_name,report,status):
    initial_resources={'water':resources['water'],'milk':resources['milk'],'coffee':resources['coffee'],'money':resources['money']}
    coffee_requirements=MENU[coffee_name.lower()]
    if coffee_requirements['milk'] < initial_resources['milk'] and coffee_requirements['water'] < initial_resources['water'] and coffee_requirements['coffee'] < initial_resources['coffee']:
        return









def Coffee_Machine():
    is_machine_on=True
    while is_machine_on:
        user_ch=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_ch == "report":
            resource_report()
        elif user_ch == "off":
            is_machine_on=False
        else:
            user_choice(user_ch)


Coffee_Machine()