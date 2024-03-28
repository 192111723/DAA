def is_perfect(number):
    return sum([i for i in range(1, number) if number % i == 0]) == number
def main():
    limit = int(input("Enter the upper limit: "))
    print("Perfect numbers up to", limit, ":")
    for i in range(1, limit + 1):
        if is_perfect(i):
            print(i)
if __name__ == "__main__":
    main()