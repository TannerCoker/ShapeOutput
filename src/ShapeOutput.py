'''
This is for testing purposes. This code will ask the user to select a shape to make and then for a number.
Then it will output the shape based on the size that was inputted.
'''

def main():
    cont = True
    print("Hello! Welcome to shape generator. Please select an option:\n\n")
    choicePrompt()
    size = getSizeInput()


#prompts user to enter a choice. displays the menu options and recieves input while testing to make sure it's valid input.
def choicePrompt():
    print("1) Square\n2) Rectangle\n3) Triangle\n4) Circle\n5) Diamond\n6) Exit\n\n")
    choice = getUserInput()
    while(not checkValidInput(choice)):
        choice = getUserInput()


def getUserInput():
    x = input("Choice: ")
    return x


def checkValidInput(x):
    if x.isdigit() and int(x) < 7 and int(x) > 0:
        return True
    elif x.isdigit():
        print("INVALID INPUT: Please select a number between 1-6")
        return False
    else:
        print('INVALID INPUT: Please enter a number')
        return False

def getSizeInput():
    x = input("Enter a size between 2 - 20: " )
    while(not checkValidSize(x)):
        x = input("Enter a size between 2 - 20: " )
    return x

def checkValidSize(size):
    if size.isdigit() and int(size) > 1 and int(size) < 21:
        return True
    elif size.isdigit():
        print("INVALID INPUT: Please select a number between 2 - 20")
        return False
    else:
        print('INVALID INPUT: Please enter a number')
        return False

main()
