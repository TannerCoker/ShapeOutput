'''
This is for testing purposes. This code will ask the user to select a shape to make and then for a number.
Then it will output the shape based on the size that was inputted.
'''

import math

def main():
    cont = True
    choice = -1
    print("Hello! Welcome to shape output.\n\n")

    while cont:
        print("Please select an option:\n")
        choice = choicePrompt()
        if int(choice) == 1:
            showSquare(getSizeInput())
        elif int(choice) == 2:
            showRect(getSizeInput())
        elif int(choice) == 3:
            showTriangle(getSizeInput())
        elif int(choice) == 6:
            cont = False
    print("\nBye!")



#prompts user to enter a choice. displays the menu options and recieves input while testing to make sure it's valid input.
def choicePrompt():
    print("1) Square\n2) Rectangle\n3) Triangle\n4) Circle\n5) Diamond\n6) Exit\n\n")
    choice = getUserInput()
    while(not checkValidInput(choice)):
        choice = getUserInput()
    return choice

#receives user input for choice
def getUserInput():
    x = input("Choice: ")
    return x

#checks for valid menu input
def checkValidInput(x):
    if x.isdigit() and int(x) < 7 and int(x) > 0:
        return True
    elif x.isdigit():
        print("INVALID INPUT: Please select a number between 1-6")
        return False
    else:
        print('INVALID INPUT: Please enter a number')
        return False

#gets valid size input
def getSizeInput():
    x = input("Enter a size between 2 - 60: " )
    while(not checkValidSize(x)):
        x = input("Enter a size between 2 - 60: " )
    return x

#checks for valid size input
def checkValidSize(size):
    if size.isdigit() and int(size) > 1 and int(size) < 61:
        return True
    elif size.isdigit():
        print("INVALID INPUT: Please select a number between 2 - 60")
        return False
    else:
        print('INVALID INPUT: Please enter a number')
        return False

#prints a square of size*size
def showSquare(size):
    print("\n\n")
    for x in range(int(size)):
        for y in range(int(size)):
            print("+ ", end='')
        print()
    print("\n\n")

#prints a rectangle of size*2size
def showRect(size):
    print("\n\n")
    for x in range(int(size)):
        for y in range(int(size)*2):
            print("+ ", end='')
        print()
    print("\n\n")

#prints a triangle of size
def showTriangle(size):
    print("\n\n")
    right = int(size)
    left = int(0)
    offset = int(math.ceil(int(size)/2))
    if int(size)%2 == 1:
        right = int(math.ceil(int(size)/2))+1+offset
        left = int(math.ceil(int(size)/2))+offset
    else:
        right = int(int(size)/2)+1+offset
        left = int(int(size)/2)+offset

    for x in range(int(size)):
        for y in range(left):
            print("  ", end ='')
        for z in range(left,right):
            print("+ ", end='')
        right += 1
        left -= 1
        print()
    print("\n\n")

main()
