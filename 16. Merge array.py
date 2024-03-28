def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        arr.clear()
        while left_half and right_half:
            arr.append(left_half.pop(0) if left_half[0] < right_half[0] else right_half.pop(0))
        arr.extend(left_half or right_half)
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)