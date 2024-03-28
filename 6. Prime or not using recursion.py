def is_prime(n, i=2):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % i == 0:
        return False 
    if i * i > n:
        return True
    return is_prime(n, i + 1)  
num = int(input("Enter a number: "))
if num < 2:
    print(num, "is not a prime number.")
elif is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")