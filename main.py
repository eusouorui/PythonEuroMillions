from ast import Pass
from calendar import c
import numbers
from sys import platform
import os

from Euromillions import Euromillions

if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')

def main():
    i = 0
    while True:
        clear()
        print("Welcome to Euromillions")
        option = menu()

        match option:
            case 1:
                createNewTicket()
                break
            case 2:
                break
            case _:
                print("Please enter a valid option")


        input()
        break

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
        print("Insert a number between " + str(min) + " and " + str(max))
        userInput = input()
        if userInput == "":
            continue
        userInt = tryParseInt(userInput)
        if userInt >= 0:
            if userInt <= max and userInt >= min:
                return userInput
        print(userInput + " is not a number between " + str(min) + " and " + str(max))
    

def menu():
    counter = 1
    print("Menu")
    print(str(counter) + " - Option 1")
    counter+=1
    print(str(counter) + " - Option 2")
    counter+=1
    print(str(counter) + " - Option 3")

    return readInt(0, counter)

def createNewTicket():
    euromillions = Euromillions()
    
    while len(euromillions.numbers) < 5:
        print(", ".join(euromillions.numbers) if len(euromillions.numbers) > 0 else "Ainda não inseriu números.")
        print(str(len(euromillions.numbers)) + "/ 5 numbers")

        


main()