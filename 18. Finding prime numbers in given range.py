def is_prime(num, divisor=2):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % divisor == 0:
        return False
    if divisor * divisor > num:
        return True
    return is_prime(num, divisor + 1)
def generate_primes(n):
    if n < 2:
        return []
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes
limit = int(input("Enter the limit: "))
print("Prime numbers up to", limit, "are:", generate_primes(limit))