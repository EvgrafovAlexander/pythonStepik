num = int(input())
i = 1
numer = 1
numercnt = 1
while i <= num:
    if numercnt > 0:
        print(numer, end=' ')
        numercnt -= 1
    else:
        numer += 1
        print(numer, end=' ')
        numercnt = numer - 1
    i += 1
