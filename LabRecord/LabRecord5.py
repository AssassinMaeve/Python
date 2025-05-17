# Write a function that returns the second-largest element in a tuple of integers.
# Add, remove, and insert elements in the list

def secondLargest(tup):
    largest = second = float('-inf')
    for i in tup:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = largest
    return second
    
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(secondLargest(tup))