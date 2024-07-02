import random
import string

def generate_password(length):
    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Prompt the user to enter the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length should be at least 1.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
