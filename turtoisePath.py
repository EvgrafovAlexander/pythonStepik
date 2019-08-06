pos = {'север' : 0, 'юг' : 0, 'восток' : 0, 'запад' : 0}
amountCommands = int(input())

for comm in range(amountCommands):
    cmd = input().split()
    pos[cmd[0]] += int(cmd[1])

print(pos['восток'] - pos['запад'], pos['север'] - pos['юг'])

#принято на Stepik