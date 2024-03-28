def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    elif len(arr) == 1:
        return arr[0], arr[0]
    else:
        mid = len(arr) // 2
        left_max, left_min = find_max_min(arr[:mid])
        right_max, right_min = find_max_min(arr[mid:])
        return max(left_max, right_max), min(left_min, right_min)
arr = [3, 1, 8, 4, 5, 2, 9, 7]
max_value, min_value = find_max_min(arr)
print("Maximum value:", max_value)
print("Minimum value:", min_value)