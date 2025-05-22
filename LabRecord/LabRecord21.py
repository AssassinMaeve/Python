def validate_password(password):
    try:
        if len(password) < 6 or len(password) > 12:
            raise ValueError("Password must be between 6 and 12 characters.")

        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter (a-z).")

        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter (A-Z).")

        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit (0-9).")

        if not any(char in "$#@" for char in password):
            raise ValueError("Password must contain at least one special character ($, #, @).")

        print("Password is valid.")
        
    except ValueError as ve:
        print("Invalid password:", ve)

# Example usage
user_password = input("Enter your password: ")
validate_password(user_password)
