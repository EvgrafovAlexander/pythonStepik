def C(n, k):
    numOfcomb = 0
    if k == 0:
        numOfcomb += 1
        return numOfcomb
    elif k > n:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


n, k = map(int, input().split())
print(C(n, k))
