# Write a menu driven program to convert
# Input string into Upper case, Lower Case, Proper case, or swap case

def menu():
    print("----Menu----")
    print("1. Convert to Upper Case")
    print("2. Convert to Lower Case")
    print("3. Convert to Proper Case")
    print("4. Convert to Swap Case")
    print("5. Exit")


def convert():
    menu()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            string = input("Enter a string: ")
            print("Upper Case:", string.upper())
        elif choice == 2:
            string = input("Enter a string: ")
            print("Lower Case:", string.lower())
        elif choice == 3:
            string = input("Enter a string: ")
            print("Proper Case:", string.title())
        elif choice == 4:
            string = input("Enter a string: ")
            print("Swap Case:", string.swapcase())
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

obj = convert()