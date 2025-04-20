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
RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def check_resources(u_ip, resources):
    if u_ip == "espresso":
        return MENU[u_ip]["ingredients"]["water"] < resources["water"] and MENU[u_ip]["ingredients"]["coffee"] < resources["coffee"]
    else:
        return MENU[u_ip]["ingredients"]["water"] < resources["water"] and MENU[u_ip]["ingredients"]["coffee"] < resources["coffee"] and MENU[u_ip]["ingredients"]["milk"] < resources["milk"]

def total_money(q, d, n, p):
    money = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return money

def enough_money(money,cost):
    if money > cost:
        return True
    else:
        return False

def give_change(money_received, cost_of_beverage):
    change = round(money_received - cost_of_beverage,2)
    return f" Here's your change: ${change}"

def adjust_inventory(money,user_input,resources):
    resources["water"] -= MENU[user_input]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
    resources["money"] += money
    if user_input == "latte" or user_input == "cappuccino":
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]

def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(f"Water: {RESOURCES["water"]}ml")
        print(f"Milk: {RESOURCES["milk"]}ml")
        print(f"Coffee: {RESOURCES["coffee"]}g")
        print(f"Money: ${RESOURCES["money"]}")
        coffee_machine()

    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_resources(u_ip=user_input, resources=RESOURCES):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            user_money = total_money(q=quarters,d=dimes,n=nickles,p=pennies)
            cost_of_beverage = MENU[user_input]["cost"]
            if enough_money(money=user_money, cost=cost_of_beverage):
                print(give_change(money_received=user_money,cost_of_beverage=cost_of_beverage))
                print(f"Here is you {user_input} ☕ Enjoy!")
                adjust_inventory(money=MENU[user_input]["cost"],user_input=user_input,resources=RESOURCES)
            else:
                print("Sorry, you haven't inserted enough money. Money refunded.")

        else:
            print("not enough resources")
        coffee_machine()
    elif user_input == "off":
        return
    else:
        print("input wasn't recognized")
        coffee_machine()

coffee_machine()
