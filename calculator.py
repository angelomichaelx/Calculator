#Michael Angelo P. Biag
#BSCOE 1-4
#CALCULATOR WITH EXCEPTIONS

def calculator():
    print("\n")

    #choosing mathematical operation that will be used based on the user ( Addition(+), Subtraction(-), Multiplication(*), Division(/))
    math_operator = input("\033[1;32m""Enter an Operator (+ - * /) : ")

    #exceptions
    try: 
        #enter First number and Second number
        firstnumber = float(input("\033[1;35m""Enter the 1st number : ")) 

        secondnumber = float(input("\033[1;35m""Enter the 2nd number : ")) 
    except ValueError as ERROR:  
         print("\033[1;31m""Invalid number input\n")
         print(ERROR)
         print("\nTry again")
         return


    #If addition
    if math_operator == "+":
        sum = firstnumber + secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(sum, 4))
        print("=" * 6)

    #If subtraction
    elif math_operator == "-":
        the_difference = firstnumber - secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(the_difference, 4))
        print("=" * 6)

    #If multiplication
    elif math_operator == "*":
        the_product = firstnumber * secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(the_product, 4))
        print("=" * 6)

    #If division
    elif math_operator == "/":
    #exception for division, if the user entered zero(0) as a divisor(2nd number)    
        try:

            the_quotient = firstnumber / secondnumber
            print("\033[1;36m" +"=" * 6)
            print(round(the_quotient, 4))
            print("=" * 6)

        except ZeroDivisionError as ERROR:
            print("\033[1;31m""Invalid equation\n")
            print(ERROR)
            print("\nTry again")
            return

    else:
        print("\033[1;31m"f"{math_operator} is not a valid operator")



# Ask the user if they want to continue on using a calculator (YES/NO)

    Repeat = input("\033[1;33m""do you want to continue on using the calculator (YES/NO) : ").upper()
    if Repeat == "YES":
            calculator()
    else:
            print("THANK YOU FOR USING THE CALCULATOR!!")
            exit()
while True:
    calculator()

