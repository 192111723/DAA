def sum_of_digits(number):
    digit_sum = 0
    number_str = str(number)
    for digit_char in number_str:
        digit = int(digit_char)
        digit_sum += digit
    return digit_sum
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits:", result)