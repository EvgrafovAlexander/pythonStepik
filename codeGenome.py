inf = open('file.txt', 'r')
genome = list(inf.readline())
inf.close()
ans = open('codeGenomeResult.txt', 'w')

curSym = ''
newSym = ''
curNum = ''
sym = 0

for el in range(len(genome)):
    if genome[el].isalpha():
        sym += 1
        if sym == 1:
            curSym = genome[el]
        if sym == 2:
            newSym = genome[el]
            print(curSym * int(curNum), end='', file=ans)
            sym = 1
            curSym = newSym
            curNum = ''
        curSym = genome[el]
    if genome[el].isdigit():
        curNum += genome[el]
    if el == len(genome) - 1:
        print(curSym * int(curNum), end='', file=ans)
