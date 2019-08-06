import requests

addr = 'https://stepic.org/media/attachments/course67/3.6.3/'
link = '699991.txt'

r = requests.get(((addr + link).strip()))
count = 0

while r.text[0] != 'W':
    r = requests.get(((addr + link).strip()))
    link = r.text
    count += 1
    print(count)
    print(link)

#принято на Stepik
