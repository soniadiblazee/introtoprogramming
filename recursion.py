# example of recursion below

def my_recursion():
    choice = input("would you like to play a game? y or n: ")
    choice = choice.lower()
    if(choice == "y"):
        my_recursion()
    elif(choice == "n"):
        print("okay, have a good day")
    else:
        print("please use 'y' or 'n' only.")
        my_recursion()

my_recursion()
# ^ start of program; program was called