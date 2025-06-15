# Step 1: Write n lines to a text file
n = int(input("Enter number of lines: "))

with open("myfile.txt", "w") as file:
    for i in range(n):
        line = input(f"Enter line {i+1}: ")
        file.write(line + "\n")

# Step 2: Display contents of the file
print("\n--- File Contents ---")
with open("myfile.txt", "r") as file:
    contents = file.read()
    print(contents)

# Step 3: Count lines, words, and characters
with open("myfile.txt", "r") as file:
    text = file.read()
    lines = text.strip().split("\n")
    words = text.split()
    characters = len(text)

print("--- File Statistics ---")
print("Number of lines     :", len(lines))
print("Number of words     :", len(words))
print("Number of characters:", characters)
