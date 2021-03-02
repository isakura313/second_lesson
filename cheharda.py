import random

players = ['Алексей', 'Сергей', 'Димон', 'Алена', 'Катя', 'Даша']

for i in range(6):
    random.shuffle(players)
    loose = players.pop(0)
    print("Выбыл", loose)
    if len(players) == 1:
        print("Win", players[0])
        break
