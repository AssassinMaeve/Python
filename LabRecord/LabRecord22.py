numbers = [5, 2, 9, 1, 7]

if numbers:
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print("Maximum:", max_num)
    print("Minimum:", min_num)
else:
    print("List is empty.")