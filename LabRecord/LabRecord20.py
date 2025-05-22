filename = "sales.txt"

n = int(input("Enter number of sales records: "))
with open(filename, "w") as f:
    for i in range(n):
        Id = input("Id: ")
        Sname = input("Salesperson Name: ")
        ProductName = input("Product Name: ")
        TotalSales = input("Total Sales: ")
        f.write(f"{Id} {Sname} {ProductName} {TotalSales}\n")

print("\nSales Details:")
with open(filename, "r") as f:
    for line in f:
        print(line)

with open(filename, "r") as f:
    data = f.read()
    lines = data.split('\n')
    words = len(data.split())
    chars = len(data)

print(f"\nNumber of lines: {len([l for l in lines if l])}")
print(f"Number of words: {words}")
print(f"Number of characters: {chars}")