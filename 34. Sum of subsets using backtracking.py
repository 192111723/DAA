def sum_of_subsets_util(arr, target_sum, subset, index, result):
    if sum(subset) == target_sum:
        result.append(subset[:])
        return
    for i in range(index, len(arr)):
        if sum(subset) + arr[i] <= target_sum:
            subset.append(arr[i])
            sum_of_subsets_util(arr, target_sum, subset, i + 1, result)
            subset.pop()
def sum_of_subsets(arr, target_sum):
    result = []
    sum_of_subsets_util(arr, target_sum, [], 0, result)
    return result
arr = [2, 4, 6, 8]
target_sum = 10
subsets = sum_of_subsets(arr, target_sum)
print("Subsets with sum equal to", target_sum, "are:")
for subset in subsets:
    print(subset)