numbers_list = [10, 5, 8, 15, 3]
max_number = lambda a, b: a if a > b else b
maximum = numbers_list[0]
for num in numbers_list[1:]:
    maximum = max_number(maximum, num)
print(maximum)