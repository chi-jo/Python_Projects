from art import logo
import random
from game_data import data

# choose random name & value as a list
def choose_name():
    item = random.choice(data)
    name = item['name']
    value = item['follower_count']
    description = item['description']
    country = item['country']
    return [name, value, description, country]

# compare two values and return the higher value & name
def compare(list_1, list_2):
    if list_1[1] > list_2[1]:
        higher = list_1
    elif list_1[1] < list_2[1]:
        higher = list_2
    else:
        higher = list_2
    return higher

# main game
def game(current_higher_item,score):
    print(f"Your current score is {score}")
    print(f"A is {current_higher_item[0]}, {current_higher_item[2]} from {current_higher_item[3]}")
    new_item = choose_name()
    print(f"B is {new_item[0]}, {new_item[2]} from {new_item[3]}")
    user_input = input("Which is higher 'A' or 'B'?: ")
    if user_input == "A":
        if compare(current_higher_item, new_item) == current_higher_item:
            score += 1
            game(current_higher_item=current_higher_item, score=score)
        else:
            print(f"Game over! Your final score is {score}")
            return
    else:
        if compare(current_higher_item, new_item) == new_item:
            score += 1
            game(current_higher_item=new_item, score=score)
        else:
            print(f"Game over! Your final score is {score}")
            return

score = 0
print(logo)
higher_item = choose_name()
game(current_higher_item=higher_item, score=score)
