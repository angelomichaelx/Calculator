#Michael Angelo P. Biag
#BSCOE 1-4

def main():

    #choosing mathematical operation that will be used based on the user ( Addition(+), Subtraction(-), Multiplication(*), Division(/))
    math_operator = input("Enter an Operator (+ - * /) : ")

    #enter First number and Second number
    firstnumber = float(input("Enter the 1st number : ")) 
    secondnumber = float(input("Enter the 2nd number : ")) 

    #If addition
    if math_operator == "+":
        sum = firstnumber + secondnumber
        print(round(sum, 4))

    #If subtraction
    elif math_operator == "-":
        the_difference = firstnumber - secondnumber
        print(round(the_difference, 4))

    #If multiplication
    elif math_operator == "*":
        the_product = firstnumber * secondnumber
        print(round(the_product, 4))

    #If division
    elif math_operator == "/":
        the_quotient = firstnumber / secondnumber
        print(round(the_quotient, 4))

    else:
        print(f"{math_operator} is not a valid operator")

# Ask the user if they want to continue on using mini calculator (YES/NO)
    Repeat = input("do you want to continue on using the calculator (YES/NO) : ").upper()
    if Repeat == "YES":
            main()
    else:
            print("THANK YOU FOR USING THE CALCULATOR!!")
            exit()
main()

