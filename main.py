from sys import platform
import os
from tkinter import N

if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')

def main():
    i = 0
    clear()
    print("Welcome to Euromillions")
    while True:
        option = menu()
        if option == 0:
            if True: #make exit function
                return

        match option:
            case 1:
                numbers, stars = createNewTicket()
                isValid, motive = validateTicket(numbers, stars)
                if(isValid) == True: 
                    print(motive)
                    print(numbers)
                    print(stars)
                else:
                    print (motive)
                break
            case 2:
                break
            case _:
                print("Please enter a valid option")
                break
        
        input("Press any key to continue...")


def tryParseInt(string, base=None):
    '''helper to parse int from string without erroring on empty or misformed string'''
    try:
        return int(string, base) if base else int(string)
    except Exception:
        return -1

def readInt(min, max):
    if min > max: 
        pass
    if min == max:
        return max
    while True:
        print("\nInsert a number between " + str(min) + " and " + str(max))
        userInput = input()
        if userInput == "":
            continue
        userInt = tryParseInt(userInput)
        if userInt >= 0:
            if userInt <= max and userInt >= min:
                return userInt
        print(userInput + " is not a number between " + str(min) + " and " + str(max))
    

def menu():
    clear()
    counter = 1
    print("Menu")
    print(str(counter) + " - Option 1")
    counter+=1
    print(str(counter) + " - Option 2")
    counter+=1
    print(str(counter) + " - Option 3")
    print("0 - Exit")

    return readInt(0, counter)

def createNewTicket():
    numbers = []
    stars = []
    while len(numbers) < 5:
        clear()
        print(numbers if len(numbers) > 0 else "No numbers insterted.")
        print(str(len(numbers)) + " / 5 numbers")
        number = readInt(1, 50)
        if number not in numbers:
            numbers.append(number)
        else:
            print("The number " + str(number) + " was already selected.")
            input("Press enter to continue...")
    
    numbers.sort()
    print("All numbers insterted\n" + str(numbers))
    input("Press enter to continue...")


    while len(stars) < 2:
        clear()
        print(stars if len(stars) > 0 else "No stars insterted.")
        print(str(len(stars)) + " / 2 stars")
        number = readInt(1, 12)
        if number not in stars:
            stars.append(number)
        else:
            print("The number " + str(number) + " was already selected.")
            input("Press enter to continue...")
    stars.sort()

    return (numbers, stars)

def validateTicket (numbers, stars):
    if len(numbers) > 5:
        return False, "Too many numbers"
    if len(numbers) < 5:
        return False, "Too litle numbers"
    if len(stars) > 2:
        return False, "Too many stars"
    if len(stars) < 2:
        return False, "Too little stars"
    if len([*filter(lambda x: x > 50, numbers)]) > 0:
        return False, "There are numbers greater than 50"
    if len([*filter(lambda x: x <= 0, numbers)]) > 0:
            return False, "There are numbers smaller than 1"
    if len([*filter(lambda x: x > 12, stars)]) > 0:
        return False, "There are stars greater than 50"
    if len([*filter(lambda x: x <= 0, numbers)]) > 0:
            return False, "There are stars smaller than 1"
    return True, "Ticket is valid"

main()