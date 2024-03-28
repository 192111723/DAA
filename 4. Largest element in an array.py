def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
            return max_element
arr = [10, 5, 20, 8, 15]
largest_element = find_largest_element(arr)
print("The largest element in the array is:", largest_element)