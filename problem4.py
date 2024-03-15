list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list(filter(lambda x: x in list1, list2))
print(intersection)