'''
soupmenu.py is a python program that utilizes a dictionary to store the inventory of different soup. User can replenish the inventory and the customer can purchase inventory.
This program mainly uses if else and while loops.
have fun running this program and do give your comments. Thanks a mil!!!
'''

#create dictionary
souplist = {}


while True:
    try:
        choice = int(input("\nPlease choose the following: \n1. Purhase Soup \n2. Replenish Soup \n3. Display Soups List \n0. Exit \n"))

        if choice == 1:
            if souplist == {}:
                print("out of stock of all soups!")
            else:
                print("\n---")
                for key in sorted(souplist.keys()):
                    print(key, "-", souplist[key])
                print("---")

                while True:
                    nameupdate = input("Please enter the soup name you would like to purchase: ")
                    if nameupdate in souplist:
                        while True:
                            try:
                                rqty = int(input("Quantity of soup to buy: "))
                                ivalue = int(souplist[nameupdate])
                                rqty = ivalue - rqty
                                souplist[nameupdate] = rqty
                                break
                            except ValueError:
                                print("Please enter valid integer")
                        break
                    else:
                        err = input("Error!!! Please enter valid soup name!!! Press any key to continue or Q to return to main menu: ")
                        err = err.upper()
                        if err == "Q":
                            break
                        else:
                            pass

        if choice == 2:
            name = str(input("Enter Soup name: "))
            while True:
                try:
                    qty = int(input("Enter quantity to replenish: "))
                    if name in souplist:
                        ivalue = int(souplist[name])
                        qty = ivalue + qty
                        souplist[name] = qty
                        print("\n---")
                        for key in sorted(souplist.keys()):
                            print(key, "-", souplist[key])
                        print("---")
                        break
                    else:
                        souplist[name] = qty
                        print("\n---")
                        for key in sorted(souplist.keys()):
                            print(key, "-", souplist[key])
                        print("---")
                        break
                except ValueError:
                    print("Please enter integer number only!!")

        if choice == 3:
            if souplist == {}:
                print("out of stock of all soups!")
            else:
                print("\n---")
                for key in sorted(souplist.keys()):
                    print(key, "-", souplist[key])
                print("---")

        if choice == 0:
            print("Goodbye")
            break

        elif choice < 0 or choice > 3:
            print("Please enter a valid input")

    except ValueError:
        print("Please enter integer only")



