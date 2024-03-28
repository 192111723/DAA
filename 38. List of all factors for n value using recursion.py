def find_factors(n, i=1, factors=[]):
    if i > n:
        return factors
    if n % i == 0:
        factors.append(i)
    return find_factors(n, i + 1, factors)
n = int(input("Enter a number: "))
all_factors = find_factors(n)
print("Factors of", n, ":", all_factors)