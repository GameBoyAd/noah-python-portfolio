#Simple Calculator

#Init

#Function
def add(num1,num2):
    result = num1 + num2
    print(result)
    print("The result is: " + str(result))

def sub(num1,num2):
    result = num1 - num2
    print(result)
    print("The result is: " + str(result))

def simple_calc():
#Main
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print("Enter an operation: ")
        print("""1.Addition
        2.Subtraction
        3.Division
        4.Multiplication
        5.Quit """)
        operation = int(input("(1-5)Operation: "))
        if operation == 1: # True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            sum = int1 + int2
            print(int1, " + ", int2, " = ", sum)

        if operation == 2: # True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            diff = int1 - int2
            print(int1, " + ", int2, " = ", diff)

        if operation == 3: # True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            Mult = int1 * int2
            print(int1, " + ", int2, " = ", Mult)

        if operation == 4: # True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            div = int1 / int2
            print(int1, " + ", int2, " = ", div)

        if operation == 5: # True
            break
#Main:
simple_calc()
