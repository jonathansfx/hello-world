# python menu loop

loop = True
while loop:
    # print main manu
    print("\nMAIN MENU")
    print("1: option 1")
    print("2: option 2")
    print("3: option 3")
    print("4: EXIT")

    # get meny selection from user
    selection = input("enter selection (1-4): ")

    # take action based on menu selection
    if selection == "1":
        print("\noption 1")
    elif selection == "2":
        print("option 2")
    elif selection == "3":
        print("option 3")
    elif selection == "4":
        print("EXIT")
        loop = False
