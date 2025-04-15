import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to add a card to the PC deck
def pc_new_card(my_list, pc_list):
    new_card = random.choice(cards)
    pc_list.append(new_card)
    if sum(pc_list) == 21:
        print(f"The sum of your cards was {sum(my_list)} & the sum of PC cards is {sum(pc_list)}")
        print("You have lost!")
    elif sum(pc_list) > 21:
        print("You won!")
        print(f"The sum of your cards was {sum(my_list)} & the sum of PC cards is {sum(pc_list)}")
    elif sum(pc_list) < 21:
        if sum(my_list) > sum(pc_list):
            print("You win!")
        elif sum(my_list) < sum(pc_list):
            print("You lose!")
        elif sum(my_list) == sum(pc_list):
            print("It's a tie?")
        print(f"The sum of your cards was {sum(my_list)} & the sum of PC cards is {sum(pc_list)}")

# Function to add cards to player's deck
def my_new_card(my_list, pc_list):
    do_you_want = input("Type 'y' or 'n' if you want or don't want a new card: ")
    if do_you_want == "y":
        new_card = random.choice(cards)
        print(f"The new card is {new_card}")
        if new_card == 11:
            ace = input("do you want a 1 or an 11?")
            if ace == "1":
                new_card = 1
            else:
                new_card = 11
        my_list.append(new_card)
        print(f"The sum of your cards is {sum(my_list)}")
        if sum(my_list) == 21:
            print("You have won!")
        elif sum(my_list) > 21:
            print("You lose!")
        elif sum(my_list) < 21:
            my_new_card(my_list, pc_list)
    else:
        pc_new_card(my_list, pc_list)

# The game comprising of the above mentioned functions
def blackjack():
    new_game = input("do you wanna play (type y or n): ")
    if new_game == "y":
        my_list = [random.choice(cards), random.choice(cards)]
        pc_list = [random.choice(cards), random.choice(cards)]
        print(f"Your cards are: {my_list}, with the sum as {sum(my_list)} & one of the PC cards are {random.choice(pc_list)}")
        if sum(my_list) == 21:
            print("You win!")
        elif sum(my_list) > 21:
            print("You lose!")
        elif sum(my_list) < 21:
            my_new_card(my_list, pc_list)
        if new_game == "y":
            blackjack()

# final command to run the program
blackjack()
