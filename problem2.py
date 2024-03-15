strings_list = ['banana', 'apple', 'grape', 'pear']
sorted_list = sorted(strings_list, key=lambda x: (len(x), x))
print(sorted_list)