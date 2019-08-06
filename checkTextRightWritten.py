amountWordsInDict = int(input())
dictWords, unknWords = dict(), dict()

for word in range(amountWordsInDict):
    dictWords[input().lower()] = 0

amountSentences = int(input())
for sentence in range(amountSentences):
    words = input().lower().split()
    for word in words:
        if word not in dictWords:
            unknWords[word] = 0

for word in unknWords:
    print(word)

#принято на Stepik