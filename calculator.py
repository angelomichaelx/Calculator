#Michael Angelo P. Biag
#BSCOE 1-4

def main():

    #choosing mathematical operation that will be used based on the user ( Addition(+), Subtraction(-), Multiplication(*), Division(/))
    math_operator = input("\033[1;32m""Enter an Operator (+ - * /) : ")

    #enter First number and Second number
    firstnumber = float(input("\033[1;31m""Enter the 1st number : ")) 
    secondnumber = float(input("Enter the 2nd number : ")) 

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
        the_quotient = firstnumber / secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(the_quotient, 4))
        print("=" * 6)

    else:
        print(f"{math_operator} is not a valid operator")

# Ask the user if they want to continue on using a calculator (YES/NO)
    Repeat = input("\033[1;33m""do you want to continue on using the calculator (YES/NO) : ").upper()
    if Repeat == "YES":
            main()
    else:
            print("THANK YOU FOR USING THE CALCULATOR!!")
            exit()
main()

