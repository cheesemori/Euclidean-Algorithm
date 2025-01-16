def main():
    """
    Main function of the program. It includes input, input check
    """
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if type(a) == int and type(b) == int:
        print(gcd(a, b))
        reuse_check()
    else:
        print("Invalid input, please try again.")
        main()

def gcd(a,b):
    """
    Secondary function. It will check the bigger number and return the result
    """
    if b > a:
        a,b=b,a
    return find_gcd(a,b)

def find_gcd(a,b):
    """
    The algorithm of the program.
    """
    if a == 0 or b == 0:
        return f"The GCD is {a+b}"
    return find_gcd(b,a % b)

def reuse_check():
    """
    This function will check if user want to use again or not.
    """
    if input("Would you like to try again? Enter 'y' to try again. ") == "y":
        main()
    else:
        print("Thanks for using!")

main()



