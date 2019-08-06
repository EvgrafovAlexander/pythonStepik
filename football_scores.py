def addToDict(dict, key, count):
    if key not in dict:
        dict[key] = count
    else:
        dict[key] += count


countFK = int(input())
cntGames = dict()
cntWins = dict()
cntLose = dict()
cntNeit = dict()
cntScore = dict()

for fk in range(countFK):
    match = input().split(';')
    #считаем количество игр
    addToDict(cntGames, match[0], 1)
    addToDict(cntGames, match[2], 1)

    addToDict(cntWins, match[0], 0)
    addToDict(cntWins, match[2], 0)
    addToDict(cntLose, match[0], 0)
    addToDict(cntLose, match[2], 0)
    addToDict(cntNeit, match[0], 0)
    addToDict(cntNeit, match[2], 0)
    addToDict(cntScore, match[0], 0)
    addToDict(cntScore, match[2], 0)

    # считаем количество побед, поражений и ничьих
    if int(match[1]) > int(match[3]):
        addToDict(cntWins, match[0], 1)
        addToDict(cntLose, match[2], 1)
        addToDict(cntScore, match[0], 3)
    elif int(match[1]) < int(match[3]):
        addToDict(cntWins, match[2], 1)
        addToDict(cntLose, match[0], 1)
        addToDict(cntScore, match[2], 3)
    else:
        addToDict(cntNeit, match[0], 1)
        addToDict(cntNeit, match[2], 1)
        addToDict(cntScore, match[0], 1)
        addToDict(cntScore, match[2], 1)

for fk in cntGames:
   print(fk, ':', cntGames[fk], ' ', cntWins[fk], ' ', cntNeit[fk], ' ', cntLose[fk], ' ', cntScore[fk], sep='')


# принято на Stepik