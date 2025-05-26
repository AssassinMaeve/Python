arr = [1,2,5,6,9,7,3]

mean = sum(arr) / len(arr)
print("Mean:", mean)

sorted_arr = sorted(arr)
n = len(arr)
if n % 2 == 1:
    median = sorted_arr[n // 2]
else:
    median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
print("Median:", median)

squared_arr = [x ** 2 for x in arr]
varience = sum(squared_arr) / len(arr)
std_div = varience ** 0.5
print("Standard Deviation:", std_div)