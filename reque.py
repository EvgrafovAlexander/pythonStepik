import requests

r = requests.get(('https://stepic.org/media/attachments/course67/3.6.2/603.txt'.strip()))
print(r.text)

print(len(r.text.splitlines()))
