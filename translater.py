alphA, alphB = input(), input()
amountSymInDict = len(alphA)

textA, textB = input(), input()
dictAtoB, dictBtoA = dict(), dict()

for sym in range(amountSymInDict):
    dictAtoB[alphA[sym]] = alphB[sym]
    dictBtoA[alphB[sym]] = alphA[sym]

resAtoB = ''
for sym in textA:
    resAtoB += dictAtoB[sym]

resBtoA = ''
for sym in textB:
    resBtoA += dictBtoA[sym]

print(resAtoB)
print(resBtoA)


#принято на Stepik