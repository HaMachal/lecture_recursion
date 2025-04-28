def recursive_nth_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)

def main():
    n = int(input("Počet členů Fibonacciho posloupnosti: "))
    seq = [recursive_nth_fibo(i) for i in range(n + 1)]
    print(seq)


if __name__ == "__main__":
    main()
