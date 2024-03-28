def order_of_number(num):
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count
def is_armstrong_recursive(num, order):
    if num == 0:
        return 0
    return ((num % 10) ** order) + is_armstrong_recursive(num // 10, order)
def is_armstrong(num):
    order = order_of_number(num)
    return num == is_armstrong_recursive(num, order)
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")