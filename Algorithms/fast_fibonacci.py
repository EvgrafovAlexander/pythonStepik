M = {0: 0, 1: 1}

def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
