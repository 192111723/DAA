def linear_search(arr, target):
    """
    Perform linear search to find the target element in the array.

    Parameters:
        arr (list): The list to be searched.
        target: The element to be searched for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [4, 2, 6, 1, 7, 9, 3]
target = 6
index = linear_search(arr, target)
if index != -1:
    print(f"Target element {target} found at index {index}.")
else:
    print(f"Target element {target} not found in the array.")