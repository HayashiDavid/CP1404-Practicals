MINIMUM_LENGTH = 10

def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)

def get_password(minimum_length):
    password = input(f"Enter the password having at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password must have at least 10 characters")
        password = input(f"Enter the password having at least {minimum_length} characters: ")
    return password

def print_asterisks(sequence):
    print('*' * len(sequence))
main()