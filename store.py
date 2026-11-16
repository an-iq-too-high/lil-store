import os
import time

money = 500
tp = 15
car = 100
human = 500
door = 350
purchases = 0
inventory = []
gpc = 750
tv = 600
sells = 0
codes = ["FREE100", "CASHBACK15", "DOORDEAL"]

while True:
    try:
        market = input("Hello! Welcome to the store, would you like to buy, sell, check your inventory, see your transactions, see your money, help, exit, see how much purchases you did, or see how much sells you did? (or 1, 2, 3, 4, 5, 6, 7, 8, or 9?) ").lower()

        if market in ["buy", "1"]:
            os.system("clear")
            buy = int(input(f"Here's the items! \n[1] Toilet Paper ${tp} \n[2] Car ${car} \n[3] Human ${human} \n[4] Door ${door} \n[5] Gaming PC ${gpc} \n[6] Flat screen TV ${tv} \nWhat item do you want? (1-5) "))

            if buy == 1:
                os.system("clear")
                print("Please wait...")

                if money < tp:
                    print("YA DONT HAVE ENOUGH MONEY, EH?")
                    break
                else:
                    money -= tp
                    inventory.append("Toilet Paper")
                    purchases += 1

                    with open("history.txt", "a") as file:
                        file.write(f"Bought: Toilet Paper (-${tp})\n")

                    os.system("clear")
                    input("Done! Press enter to go back!")
                    os.system("clear")
                    continue

            elif buy == 2:
                os.system("clear")
                print("Please wait...")

                if money < car:
                    print("YA DONT HAVE ENOUGH MONEY, EH?")
                    break
                else:
                    money -= car
                    inventory.append("Car")
                    purchases += 1

                    with open("history.txt", "a") as file:
                        file.write(f"Bought: Car (-${car})\n")

                    os.system("clear")
                    input("Done! Press enter to go back!")
                    os.system("clear")
                    continue

            elif buy == 3:
                os.system("clear")
                print("Please wait...")

                if money < human:
                    print("YA DONT HAVE ENOUGH MONEY, EH?")
                    break
                else:
                    money -= human
                    inventory.append("Human")
                    purchases += 1

                    with open("history.txt", "a") as file:
                        file.write(f"Bought: Human (-${human})\n")

                    os.system("clear")
                    input("Done! Press enter to go back!")
                    os.system("clear")
                    continue

            elif buy == 4:
                os.system("clear")
                print("Please wait...")

                if money < door:
                    print("YA DONT HAVE ENOUGH MONEY, EH?")
                    break
                else:
                    money -= door
                    inventory.append("Door")
                    purchases += 1

                    with open("history.txt", "a") as file:
                        file.write(f"Bought: Door (-${door})\n")

                    os.system("clear")
                    input("Done! Press enter to go back!")
                    os.system("clear")
                    continue
            elif buy == 5:
                os.system("clear")
                print("Please wait...")

                if money < gpc:
                    print("YA DONT HAVE ENOUGH MONEY, EH?")
                    break
                else:
                    money -= gpc
                    inventory.append("Gaming Pc")
                    purchases += 1

                    with open("history.txt", "a") as file:
                        file.write(f"Bought: Gaming PC (-${gpc})\n")

                    os.system("clear")
                    input("Done! Press enter to go back!")
                    os.system("clear")
                    continue
            
            elif buy == 6:
                os.system("clear")
                print("Please wait...")

                if money < tv:
                    print("YA DONT HAVE ENOUGH MONEY, EH?")
                    break
                else:
                    money -= tv
                    inventory.append("Tv")
                    purchases += 1

                    with open("history.txt", "a") as file:
                        file.write(f"Bought: TV (-${tv})\n")

                    os.system("clear")
                    input("Done! Press enter to go back!")
                    os.system("clear")
                    continue

            else:
                os.system("clear")
                input("Please enter a number!")
                os.system("clear")
                continue

        elif market in ["sell", "2"]:
            os.system("clear")
            item = input("What is the item you'd like to sell? ").title()

            if item in inventory:
                price = int(input("How much is it? "))

                if price < 0:
                    os.system("clear")
                    print("Do not do it under 0!")
                    continue

                elif price < 1000:
                    hmm = input(f"Are you SURE you want to sell {item}? ").lower()

                    if hmm == "yes":
                        print("Please wait...")
                        money += price
                        inventory.remove(item)
                        sells += 1

                        with open("history.txt", "a") as file:
                            file.write(f"Sold: {item} (+${price})\n")

                        os.system("clear")
                        input("Thank you! ")
                        os.system("clear")
                        continue

                    elif hmm == "no":
                        os.system("clear")
                        continue

                    else:
                        os.system("clear")
                        print("Please enter yes or no!")
                        continue

                elif price >= 1000:
                    print("Yeah.... No thank you")
                    break

            else:
                os.system("clear")
                print("You don't have this item! Check your inventory for items!")

        elif market in ["inventory", "3"]:
            os.system("clear")
            print(inventory)
            time.sleep(5)
            os.system("clear")
            continue

        elif market in ["transactions", "4"]:
            try:
                with open("history.txt", "r") as file:
                    print(file.read())
                    delete_or_no = input("\nDo you want to delete transactions?").lower()

                    if delete_or_no == "yes":
                        print("Deleting...")

                        with open("history.txt", "w") as file:
                            pass

                        time.sleep(3)
                        input("Deleted! Press enter to escape!")
                        os.system("clear")
                        continue

                    elif delete_or_no == "no":
                        input("Ok! Press enter to escape!")
                        os.system("clear")
                        continue

                    else:
                        os.system("clear")
                        print("Please enter yes or no!")
                        continue

            except FileNotFoundError:
                os.system("clear")
                print("No transaction history yet!")
                time.sleep(3)
                os.system("clear")

        elif market in ["money", "5"]:
            os.system("clear")
            print(f"${money}")
            time.sleep(5)
            os.system("clear")
            continue

        elif market in ["help", "6"]:
            os.system("clear")
            print("Commands: buy, sell, inventory, transactions, money, help, exit")
            time.sleep(5)
            os.system("clear")

        elif market in ["exit", "7"]:
            os.system("clear")
            raise SystemExit

        elif market in ["purchases", "8"]:
            os.system("clear")
            print("Please wait...")

            if purchases == 0:
                os.system("clear")
                input("You dont have purchases!")
                os.system("clear")
                continue

            else:
                os.system("clear")
                print(purchases)
                time.sleep(5)
                os.system("clear")
                continue
        elif market in ["sells", "9"]:
            os.system("clear")
            print("Please wait...")
            
            if sells == 0:
                os.system("clear")
                input("You did not sell anything yet!")
                os.system("clear")
                continue
            else:
                os.system("clear")
                print(sells)
                time.sleep(5)
                os.system("clear")
                continue
        elif market in ["redeem", "10"]:
            code = input("Enter your code: ").upper()
            
            if code == "FREE100" and code in codes:
                os.system("clear")
                print("Please wait...")
                money += 100
                codes.remove(code)
                os.system("clear")
                input("SUCCESS! You received $100!")
                os.system("clear")
                continue

            elif code == "CASHBACK15" and code in codes:
                os.system("clear")
                print("Please wait...")
                tp *= 0.15
                car *= 0.15
                human *= 0.15
                gpc *= 0.15
                door *= 0.15
                codes.remove(code)
                os.system("clear")
                input("SUCCESS! You unlocked 15% cashback!")
                os.system("clear")
                continue
            elif code == "DOORDEAL" and code in codes:
                os.system("clear")
                print("Please wait...")
                door = 0
                os.system("clear")
                codes.remove(code)
                input("SUCCESS! Check the market!")
                os.system("clear")
                continue

            else:
                print("Invalid or already used code!")
            

        else:
            print("Please say a number or word!")
            continue

    except ValueError:
        print("Enter a number! Now exiting……")
        break
