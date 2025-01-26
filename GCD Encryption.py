def reuse():
    # Ask the user if they want to reuse the program
    judge = input("Would you like to reuse? (y/n) ")
    if judge == "y":
        main()  # Re-run the main function
    elif judge == "n":
        print("Thank you for using Euclidean Algorithm!")  # Exit message
        exit()  # Exit the program
    else:
        print("Invalid input! please try again")  # Check invalid input
        reuse()  # Retry asking the user

def encryption():
    # Encryption process
    m = int(input("Enter a original number: "))  # Input the original number
    k = int(input("Enter a encryption key number: "))  # Input the encryption key
    n = k * 2 + 1  # Calculate modulus based on the key

    # Output encryption result
    print(f"Your original number is: {m} \nYour encryption key is: {k} \nYour encryption result is: {(m * k) % n}")

def decryption():
    # Decryption process
    c = int(input("Enter your encryption result number: "))  # Input the encrypted result
    k = int(input("Enter your decryption key number: "))  # Input the decryption key
    n = k * 2 + 1  # Calculate modulus based on the key

    # Function to calculate modular inverse using the extended Euclidean algorithm
    def modular_inverse(k, n):
        # Extended Euclidean algorithm
        def extended_gcd(a, b):
            if b == 0:
                return a, 1, 0  
            gcd, x1, y1 = extended_gcd(b, a % b)  
            x = y1  # Update x
            y = x1 - (a // b) * y1  # Update y
            return gcd, x, y

        gcd, x, y = extended_gcd(k, n)  # Call extended Euclidean algorithm
        if gcd != 1:  # Check if modular inverse exists
            print("Incorrect encryption result or decryption key!")  # Error message
            reuse()  # Retry the program
        return x % n  # Return the modular inverse and make sure it is not negative

    key_inv = modular_inverse(k, n)  # Compute the modular inverse of the decryption key
    print(f"The decryption result is {(c * key_inv) % n}")  # Output decryption result

def main():
    # Main function to choose between encryption and decryption
    judge = input("Please choose an algorithm:\n  1.encryption algorithm\n  2.decryption algorithm\n")
    if judge == "1":
        encryption()  # Call encryption function
        reuse()  # Ask if the user wants to reuse the program
    elif judge == "2":
        decryption()  # Call decryption function
        reuse()  # Ask if the user wants to reuse the program
    else:
        print("Invalid input! please try again")  # Check invalid input
        main()  # Retry asking the user

main()  # Start the program
