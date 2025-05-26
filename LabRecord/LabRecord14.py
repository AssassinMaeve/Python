def sum_avg_list(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers) if numbers else 0
    print("List Sum:", total)
    print("List Average:", avg)

def sum_avg_tuple(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers) if numbers else 0
    print("Tuple Sum:", total)
    print("Tuple Average:", avg)

# Example usage
lst = [1, 2, 3, 4, 5]
tpl = (10, 20, 30, 40)

sum_avg_list(lst)
sum_avg_tuple(tpl)