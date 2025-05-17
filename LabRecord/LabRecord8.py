# Create two sets containing ‘n’ elements, using menu
# driven approach Perform all the basic operations on both the sets

def inputSet():
    set1 = set()
    set2 = set()
    n = int(input("Enter the number of elements in the set: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        set1.add(element)

    n = int(input("Enter the number of elements in the second set: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        set2.add(element)
    return set1, set2

def menu():
    print("----Menu----")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Symmetric Difference")
    print("5. Subset")
    print("6. Superset")
    print("7. Exit")

def setOperations(set1, set2):
    menu()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Union:", set1.union(set2))
        elif choice == 2:
            print("Intersection:", set1.intersection(set2))
        elif choice == 3:
            print("Difference:", set1.difference(set2))
        elif choice == 4:
            print("Symmetric Difference:", set1.symmetric_difference(set2))
        elif choice == 5:
            print("Subset:", set1.issubset(set2))
        elif choice == 6:
            print("Superset:", set1.issuperset(set2))
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

set1, set2 = inputSet()
setOperations(set1, set2)