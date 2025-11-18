import random

n, m = 10, 10
rooms = ["#", "s", "m", "l"]# пустая,сундук,монстр,ловушка
real_map = [[random.choice(rooms) for j in range(m)] for i in range(n)]# создаем реальную таблицу с помощью 2 генераторов

empty_cells = [(i, j) for i in range(n) for j in range(m) if real_map[i][j] == "#"]# список с пустыми клетками для спавна
if not empty_cells:
    raise Exception("Нет ни одной пустой клетки для спавна!Попробуйте еще раз")

start_x, start_y = random.choice(empty_cells)# выбираем рандомную клетку для спавна
# комната с ключом и порталом должна быть единственная, поэтому создадим их отдельно
while True:
    kx, ky = random.randint(0, n-1), random.randint(0, m-1)
    if (kx, ky) != (start_x, start_y):
        real_map[kx][ky] = "k"# если случайная клетка не спавн ставим туда комнату с ключом
        break
while True:
    px, py = random.randint(0, n-1), random.randint(0, m-1)
    if (px, py) != (start_x, start_y) and (px, py) != (kx, ky):
        real_map[px][py] = "p"# если случайная клетка не спавн и не комната с ключом ставим туда портал
        break

visible_map = [[False for _ in range(m)] for __ in range(n)]# список, который хранит информацию о посещении клетки
health = 100
inventory = []
visible_map[start_x][start_y] = True# стартовую клетку мы посетили

def display_map(real_map, visible_map, player_x, player_y):# создаем матрицу, которая видна игроку
    for i in range(n):
        row = ""# создаем нашу пустую строку
        for j in range(m):
            if i == player_x and j == player_y:
                row += "@ "# если это координата, где мы находимся, ставим @
            elif visible_map[i][j]:
                row += real_map[i][j] + " "# если в этой клетке мы были, выводим название этой комнаты
            else:
                row += "* "
        print(row)

def can_move(x, y):
    return 0 <= x < n and 0 <= y < m#не уперлись ли мы в стену

def process_cell(cell, health, inventory, x, y):
    if cell == "#":
        print("Пустая комната.")
    elif cell == "s":# если наткнулись на сундук, либо + рандомное хп, либо меч
        effect = random.choice(["hp", "sword"])
        if effect == "hp":
            heal = random.randint(10, 30)
            health += heal
            print(f"Вы нашли сундук и получили +{heal} к здоровью.")
        else:
            inventory.append("меч")
            print("Вы нашли сундук и получили меч.")
        real_map[x][y] = "#"  # После первого визита комната становится пустой, чтобы игроки бесконечно не  добавляли себе предметы
    elif cell == "m":# комната с монстром, если есть меч, делаем комнату пустой, если нет, теряем здоровье
        if "меч" in inventory:
            inventory.remove("меч")
            print("Вы встретили монстра, но использовали меч для победы.")
        else:
            damage = random.randint(5, 20)
            health -= damage
            print(f"Монстр атаковал! Вы потеряли {damage} здоровья.")
        real_map[x][y] = "#"  # После первого визита комната становится пустой
    elif cell == "l":# ловушка, минус к хп
        health -= 10
        print("Вы наступили на ловушку и потеряли 10 здоровья.")
    elif cell == "k":# комната с ключом, кладем его в инвентарь
        if "ключ" not in inventory:
            inventory.append("ключ")
            print("Вы нашли ключ и положили его в инвентарь.")
        else:
            print("Здесь уже был ключ.")
    elif cell == "p":# комната с порталом, если есть ключ - победа, если нет продолжаем
        if "ключ" in inventory:
            print("Вы использовали ключ и прошли через портал! Победа!")
            return health, inventory, True
        else:
            print("Это портал, но у вас нет ключа.")
    return health, inventory, False

# чисто технические моменты, отображаем здоровье и инвентарь, помогаем пользователю в управлении
player_x, player_y = start_x, start_y
victory = False

while health > 0 and not victory:
    print(f"\nЗдоровье: {health}, Инвентарь: {inventory}")
    display_map(real_map, visible_map, player_x, player_y)
    move = input("Введите направление (w - вверх, s - вниз, a - влево, d - вправо): ")
    new_x, new_y = player_x, player_y
    if move == "w":
        new_x -= 1
    elif move == "s":
        new_x += 1
    elif move == "a":
        new_y -= 1
    elif move == "d":
        new_y += 1
    else:
        print("Неверное направление, попробуйте снова.")
        continue
# если можем двигаться, задаем новые значения координат, открываем клетку, вызываем функцию уже с новыми значениями
    if can_move(new_x, new_y):
        player_x, player_y = new_x, new_y
        visible_map[player_x][player_y] = True
        health, inventory, victory = process_cell(
            real_map[player_x][player_y], health, inventory, player_x, player_y
        )
    else:
        print("Вы уперлись в стену.")

if health <= 0:
    print("У вас закончилось здоровье. Игра окончена.")
elif victory:
    print("Поздравляем! Вы выиграли игру.")
