import random

list = ('R', 'P', 'S')

while True:


    print("lets play rock paper scissors \n")

    while True:
        choice = input("Type R to choose rock\n     P to choose paper\n     S to choose scissors \n ")
        if choice != 'R' and choice != 'P' and choice != 'S':
            print("\nWrong input please try again\n")
        else:
            break

    rand = random.choice(list)

    if choice == rand:
        print("Your choice is " + choice + " and Computer choice is " + rand + "\n\nIts a tie!")
    elif choice == 'R' and rand == 'S':
        print("Your choice is " + choice + " and Computer choice is " + rand + "\n\nYou win!")
    elif choice == 'S' and rand == 'P':
        print("Your choice is " + choice + " and Computer choice is " + rand + "\n\nYou win!")
    elif choice == 'P' and rand == 'R':
        print("Your choice is " + choice + " and Computer choice is " + rand + "\n\nYou win!")
    else:
        print("Your choice is " + choice + " and Computer choice is " + rand + "\n\nYou lose!")

    check = input("\nType a if you like to play again \n")
    if check != 'a':
        break
