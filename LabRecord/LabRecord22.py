import numpy as np

# Step 1: Create a NumPy array of random integers between 1 and 100
data = np.random.randint(1, 101, size=15)
print("Original Array:")
print(data)

# Step 2: Fancy Indexing - Extract elements at specific positions
positions = [0, 3, 5, 7, 10]
fancy_selected = data[positions]
print("\nElements at positions", positions, ":")
print(fancy_selected)

# Step 3: Masking - Find and display all elements greater than 50
mask = data > 50
print("\nElements greater than 50:")
print(data[mask])

# Step 4: Masking - Replace all odd numbers with -1
odd_mask = data % 2 == 1
data[odd_mask] = -1
print("\nArray after replacing odd numbers with -1:")
print(data)