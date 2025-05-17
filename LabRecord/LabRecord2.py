# Create a tuple with different data types and print each element.
# Check if an element exists in a tuple.

tup = (1, 2.5, "Hello")
print("Tuple:", tup)

search = 2.5
if search in tup:
    print(f"{search} exists in the tuple.")
else:
    print(f"{search} does not exist in the tuple.")