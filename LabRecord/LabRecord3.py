# Create an empty list. Input ‘n’ items.
# Count total number of Odd, Even, and zero items in the list and display the contents of new lists

number = int(input("Enter the number of items in the list: "))
numbers = []

for i in range(number):
    item = int(input(f"Enter the items in the list ({i + 1}/{number}): "))
    numbers.append(item)
print("List:", numbers)

even = []
odd = []
zero = []

for i in numbers:
    if i == 0:
        zero.append(i)
    elif i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Zero numbers:", zero)
print("Total even numbers:", len(even))
print("Total odd numbers:", len(odd))
print("Total zero numbers:", len(zero))
