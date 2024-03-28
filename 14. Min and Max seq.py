def min_max_sequence(numbers):
    if not numbers:
        return "List is empty"
    min_sequence = [numbers[0]]
    max_sequence = [numbers[0]]
    min_value = numbers[0]
    max_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
            min_sequence.append(num)
        elif num > max_value:
            max_value = num
            max_sequence.append(num)
    return min_sequence, max_sequence
numbers = [5, 10, 3, 8, 15, 2, 7]
min_sequence, max_sequence = min_max_sequence(numbers)
print("Minimum value sequence:", min_sequence)
print("Maximum value sequence:", max_sequence)