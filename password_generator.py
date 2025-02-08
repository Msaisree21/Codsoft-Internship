import random
import string
def generate_password(length):
    if not isinstance(length, int) or length <= 0:
        return "Invalid length. Please enter a positive integer."
    characters = string.ascii_letters + string.digits + string.punctuation  
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def main():
    while True:  
        try:
            length = int(input("Enter the desired length of the password (or 0 to exit): "))
            if length == 0:
              break 
            password = generate_password(length)
            print("Generated Password:", password)
        except ValueError:
            print("Invalid input. Please enter an integer for the length.")
        except Exception as e: 
            print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

