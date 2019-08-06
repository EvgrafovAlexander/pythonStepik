a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d + 1):
    print('\t', i, end='')
print('')
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        if j != d:
            print(i * j, end='\t')
        else:
            print(i * j, end='')
    print('')
