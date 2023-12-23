import random
import time

money = 5000
money_in_the_bank = 0

hour = 8

on_israel = True
on_turkey = False
on_egypt = False

#      copper olives wheat
inventory = [0, 0, 0]

def prices_menu(copper_prices, olives_prices, wheat_prices):


    if on_israel:
        print("         turkey               ~israel~            egypt")
    if on_egypt:
        print("         turkey                israel             ~egypt~")
    if on_turkey:
        print("        ~turkey~               israel              egypt")
    print("copper - " + str(copper_prices[0]) + "                 " + str(copper_prices[1]) + "                " + str(copper_prices[2]))
    print("olives - " + str(olives_prices[0]) + "                  " + str(olives_prices[1]) + "                 " + str(olives_prices[2]))
    print("wheat -  " + str(wheat_prices[0]) + "                   " + str(wheat_prices[1]) + "                  " + str(wheat_prices[2]))

def buy_menu(copper_prices, olives_prices, wheat_prices):
    global money
    option = 0
    print("what do you want to buy?\n")
    print("1 - copper\n2 - olives\n3 - wheat\n")
    option = input("Enter your choice: ")

    if option.isdigit():
        option = int(option)

        if option == 1:
            buy_copper(copper_prices)
        elif option == 2:
            buy_olives(olives_prices)
        elif option == 3:
            buy_wheat(wheat_prices)

def buy_copper(copper_prices):
    global money
    number_of_items = 0

    if on_israel:
        print("max - " + str(int(money / copper_prices[1])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * copper_prices[1] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[0] += number_of_items
            money -= number_of_items * copper_prices[1]

    elif on_turkey:
        print("max - " + str(int(money / copper_prices[0])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * copper_prices[0] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[0] += number_of_items
            money -= number_of_items * copper_prices[0]

    elif on_egypt:
        print("max - " + str(int(money / copper_prices[2])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * copper_prices[2] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[0] += number_of_items
            money -= number_of_items * copper_prices[2]

def buy_olives(olives_prices):
    global money
    number_of_items = 0

    if on_israel:
        print("max - " + str(int(money / olives_prices[1])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * olives_prices[1] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[1] += number_of_items
            money -= number_of_items * olives_prices[1]

    elif on_turkey:
        print("max - " + str(int(money / olives_prices[0])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * olives_prices[0] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[1] += number_of_items
            money -= number_of_items * olives_prices[0]

    elif on_egypt:
        print("max - " + str(int(money / olives_prices[2])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * olives_prices[2] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[1] += number_of_items
            money -= number_of_items * olives_prices[2]

def buy_wheat(wheat_prices):
    global money
    number_of_items = 0

    if on_israel:
        print("max - " + str(int(money / wheat_prices[1])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * wheat_prices[1] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[2] += number_of_items
            money -= number_of_items * wheat_prices[1]

    elif on_turkey:
        print("max - " + str(int(money / wheat_prices[0])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * wheat_prices[0] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[2] += number_of_items
            money -= number_of_items * wheat_prices[0]

    elif on_egypt:
        print("max - " + str(int(money / wheat_prices[2])))
        number_of_items = int(input("how many do you want to buy: "))

        if number_of_items * wheat_prices[2] > money:
            print("you dont have enough money.")
        elif number_of_items < 1:
            print("you cant buy less then 1")
        else:
            inventory[2] += number_of_items
            money -= number_of_items * wheat_prices[2]

def sell_menu(copper_prices, olives_prices, wheat_prices):
    global money
    global inventory

    option = 0

    print("what do you want to sell?\n")
    print("1 - copper\n2 - olives\n3 - wheat\n")
    option = input("Enter your choice: ")

    if(option.isdigit()):
        option = int(option)
        if option == 1:
            sell_copper(copper_prices)
        elif option == 2:
            sell_olives(olives_prices)
        elif option == 3:
            sell_wheat(wheat_prices)

def sell_copper(copper_prices):
    global money
    number_of_items = 0

    if on_israel:
        print("max - " + str(inventory[0]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[0]:
            print("you dont have enough items.")
        else:
            inventory[0] -= number_of_items
            money += number_of_items * copper_prices[1]

    elif on_turkey:
        print("max - " + str(inventory[0]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[0]:
            print("you dont have enough items.")
        else:
            inventory[0] -= number_of_items
            money += number_of_items * copper_prices[0]

    elif on_egypt:
        print("max - " + str(inventory[0]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[0]:
            print("you dont have enough items.")
        else:
            inventory[0] -= number_of_items
            money += number_of_items * copper_prices[2]

def sell_olives(olives_prices):
    global money
    number_of_items = 0

    if on_israel:
        print("max - " + str(inventory[1]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[1]:
            print("you dont have enough items.")
        else:
            inventory[1] -= number_of_items
            money += number_of_items * olives_prices[1]

    elif on_turkey:
        print("max - " + str(inventory[1]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[1]:
            print("you dont have enough items.")
        else:
            inventory[1] -= number_of_items
            money += number_of_items * olives_prices[0]

    elif on_egypt:
        print("max - " + str(inventory[1]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[1]:
            print("you dont have enough items.")
        else:
            inventory[1] -= number_of_items
            money += number_of_items * olives_prices[2]

def sell_wheat(wheat_prices):
    global money
    number_of_items = 0

    if on_israel:
        print("max - " + str(inventory[2]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[2]:
            print("you dont have enough items.")
        else:
            inventory[2] -= number_of_items
            money += number_of_items * wheat_prices[1]

    elif on_turkey:
        print("max - " + str(inventory[2]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[2]:
            print("you dont have enough items.")
        else:
            inventory[2] -= number_of_items
            money += number_of_items * wheat_prices[0]

    elif on_egypt:
        print("max - " + str(inventory[2]))
        number_of_items = int(input("how many do you want to sell: "))

        if number_of_items > inventory[2]:
            print("you dont have enough items.")
        else:
            inventory[2] -= number_of_items
            money += number_of_items * wheat_prices[2]

def bank():
    global money_in_the_bank
    global money
    option = 0

    print("what do you want to do?\n1 - Deposit\n2 - Withdrawal")
    option = int(input("Enter your choice: "))

    if option == 1:
        amount = int(input("How much do you want to deposit? "))
        
        if amount > money:
            print("you dont have enough money.")
        elif amount < 1:
            print("you cant deposit less then 1.")
        else:
            money -= amount
            money_in_the_bank += amount

    elif option == 2:
        print("you have " + str(money_in_the_bank) + "in the bank")

        amount = int(input("How much do you want to withdraw? "))
        
        if amount > money:
            print("you dont have enough money.")
        elif amount < 1:
            print("you cant withdrawal less then 1.")
        else:
            money += amount
            money_in_the_bank -= amount

def storm_strike(copper_prices, olives_prices, wheat_prices, reason):
    global on_egypt
    global on_israel
    global on_turkey
    global hour
    
    if(on_israel):
        print("Because of a "+ reason +", you are back in Israel.")
    elif(on_egypt):
        print("Because of a "+ reason +", you are back in Egypt.")
    elif(on_turkey):
        print("Because of a "+ reason +", you are back in Turkey.")
        
    hour += 8
    time.sleep(3)
    main_menu(copper_prices, olives_prices, wheat_prices)

def mistake(copper_prices, olives_prices, wheat_prices):
    global on_egypt
    global on_israel
    global on_turkey
    global hour
    events = random.randint(0, 30)

    if(on_israel):
        if(events < 10):
            print("Because of a mistake, you arrive to Turkey")
            on_israel = False
            on_turkey = True
            on_egypt = False
        elif(events < 10 and events > 20):
            print("Because of a mistake, you arrive to Egypt")
            on_israel = False
            on_turkey = False
            on_egypt = True
        else:
            print("Because of a mistake, you arrive to Israel")
    elif(on_egypt):
        if(events < 10):
            print("Because of a mistake, you arrive to Turkey")
            on_israel = False
            on_turkey = True
            on_egypt = False
        elif(events < 10 and events > 20):
            print("Because of a mistake, you arrive to Israel")
            on_israel = True
            on_turkey = False
            on_egypt = False
        else:
            print("Because of a mistake, you arrive to Egypt")
    elif(on_turkey):
        if(events < 10):
            print("Because of a mistake, you arrive to Egypt")
            on_israel = False
            on_turkey = False
            on_egypt = True
        elif(events < 10 and events > 20):
            print("Because of a mistake, you arrive to Israel")
            on_israel = True
            on_turkey = False
            on_egypt = False
        else:
            print("Because of a mistake, you arrive to Egypt")
    hour += 8

    time.sleep(3)
    main_menu(copper_prices, olives_prices, wheat_prices)

def pirates():
    global money
    global inventory
    print("pirates!")
    print("What do you want to do: ")
    print("1 - ")
    print("2 - ")
    print("3 - ")
    option = int(input(">>> "))


def sail(copper_prices, olives_prices, wheat_prices):
    # TODO add a sail system that thing can happen randomly
    option = 0
    global on_israel
    global on_turkey
    global on_egypt
    global hour
    events = random.randint(1, 100)

    print("where do you want to go?\n1 - turkey\n2 - Israel\n3 - Egypt")
    option = input("Enter your choice: ")

    if(option.isdigit()):
        option = int(option)

        if(hour == 20 or hour + 8 > 20):
            print("its too late you cannot go!")
        else:

            time.sleep(3)

            if(events < 5):
                storm_strike(copper_prices, olives_prices, wheat_prices, "strike")
            elif(events > 5 and events < 10):
                mistake(copper_prices, olives_prices, wheat_prices)
            elif(events > 10 and events < 20):
                print("natosh")
            elif(events > 20 and events < 35):
                storm_strike(copper_prices, olives_prices, wheat_prices, "storm")
            elif(events > 35 and events < 60):
                pirates()
            else:
                if option == 1:
                    if(on_egypt == True):
                        hour += 8
                    else:
                        hour += 4
                    on_israel = False
                    on_turkey = True
                    on_egypt = False

                    main_menu(copper_prices, olives_prices, wheat_prices)

                elif option == 2:
                    hour += 4
                    on_israel = True
                    on_turkey = False
                    on_egypt = False

                    main_menu(copper_prices, olives_prices, wheat_prices)

                elif option == 3:
                    if(on_turkey == True):
                        hour += 8
                    else:
                        hour += 4
                    on_israel = False
                    on_turkey = False
                    on_egypt = True

                    main_menu(copper_prices, olives_prices, wheat_prices)

def main_menu(copper_prices, olives_prices, wheat_prices):
    option = 0
    global money
    global hour
    global on_israel
    global on_turkey
    global on_egypt

    while(True):
        print("Money - " + str(money))
        print("hour - " + str(hour) + ":00")
        print("copper - " + str(inventory[0]))
        print("olives - " + str(inventory[1]))
        print("wheat - " + str(inventory[2]))
        print("\n")

        print("your options:\n")
        print("1 - Buy\n")
        print("2 - Sell\n")
        print("3 - Sail\n")
        print("4 - Go ot the bank\n")
        print("5 - Rest until tomorrow\n")

        print("prices:")
        # print the prices menu
        prices_menu(copper_prices, olives_prices, wheat_prices)

        
        option = input("Enter your choice: ")
        if(option.isdigit()):
            option = int(option)
            if option == 1:
                buy_menu(copper_prices, olives_prices, wheat_prices)
            elif option == 2:
                sell_menu(copper_prices, olives_prices, wheat_prices)
            elif option == 3:
                sail(copper_prices, olives_prices, wheat_prices)
            elif option == 4:
                bank()
            elif option == 5:
                break

def main():
    print("title\n")

    time.sleep(3)
    
    global money
    global hour
    global on_israel
    global on_turkey
    global on_egypt

    for day in range(1, 8):
        hour = 8
        if day == 7:
            # a massege for the last day
            print("\n\n\n\n")
            print("This is the last day.\nremember to sell all your goods because your final score will be counted by the amount of money you have at the end of the day.")
            time.sleep(5)
        print("\n\n\n\n")
        print("welcome to the " + str(day) + " trading day.\n")
        time.sleep(3)

        # define all the prices for today
        #               turkey                   israel                  egypt
        wheat_prices = [random.randint(30, 70), random.randint(30, 70), random.randint(30, 70)]
        olives_prices = [random.randint(300, 600), random.randint(300, 600), random.randint(300, 600)]
        copper_prices = [random.randint(2000, 4000), random.randint(2000, 4000), random.randint(2000, 4000)]

        # print the main menu
        main_menu(copper_prices, olives_prices, wheat_prices)
    # the end screen
    print("\n\n\n\n")
    print("The End!")
    print("your score is - " + str(money) + ". congrats! 🎉")
    

if __name__ == "__main__":
    main()