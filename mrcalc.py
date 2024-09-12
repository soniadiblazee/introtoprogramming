# try/except function checks for errors!
# return function tells code to stop function and sends 
# the function's result back to the caller!!
# break exits a loop!!!

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 /num2

def expodent(num1, num2):
    return num1 ** num2


print("what math would you like to try?")
print("1. addition, 2. subtraction, 3. multiplication, 4. division, 5. expodent")

while True:
    choice = input("enter your choice (1,2,3,4,5): ")

    if (choice == '1' '2' '3' '4' '5'):
        try:
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
        except ValueError:
            print("invalid input. please choose a number from the list.")

            if choice == '1':
                print(num1, '+', num2, '=', add(num1, num2))
            elif choice == '2':
                print(num1, '-', num2, '=', subtract(num1, num2))
            elif choice == '3':
                print(num1, '*', num2, '=', multiply(num1, num2))
            elif choice == '4':
                print(num1, '/', num2, '=', divide(num1, num2))
            elif choice == '5':
                print(num1, '**', num2, '=', expodent(num1, num2))

            next_calculation = input("another? (yes/no)")
            if next_calculation == "no":
                break
        else:
            print("invalid input")