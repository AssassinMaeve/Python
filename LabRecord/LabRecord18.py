try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter integers only.")
except ZeroDivisionError:
    print("Cannot divide by zero!")