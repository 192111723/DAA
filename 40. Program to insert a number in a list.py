original_list = [1, 2, 3, 4, 5]
index = 2
number = 10
if index < 0 or index > len(original_list):
    print("Index out of range.")
else:
    original_list.insert(index, number)
    print("Modified list:", original_list)