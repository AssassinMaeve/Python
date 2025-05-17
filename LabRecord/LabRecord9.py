# Write Python program to Accept string and count the total number of vowels, consonants and blanks in a String.      
# (Use Assert statement to accept strings only)

s = input("Enter a string: ")
assert isinstance(s, str), "Input must be a string"

vowels = 0
consonants = 0
blanks = 0

for char in s:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char == ' ':
        blanks += 1
    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Blanks:", blanks)