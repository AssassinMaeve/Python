# Create a List in Integers and perform linear search on the list to find a number which is user input

lst = [1,2,3,4,5,6,7,8,9]
search = int(input("Enter the number to search: "))

for i in range(len(lst)):
    if lst[i] == search:
        print(f"{search} found at index {i}")
        break