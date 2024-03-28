def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def print_fibonacci_series(count):
    for i in range(count):
        print(fibonacci(i), end=" ")
n_terms = 10
print("Fibonacci Series:")
print_fibonacci_series(n_terms)