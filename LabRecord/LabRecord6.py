# Write a Python function that takes a list of integers as parameter and function
# should return the maximum and minimum numbers from the list. (don’t use built-in methods)

def findMaxMin(lst):
    max = min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("List:", lst)
print(f"Maximum: {findMaxMin(lst)[0]} Minimum: {findMaxMin(lst)[1]}")