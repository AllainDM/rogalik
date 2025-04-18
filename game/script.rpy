# Инициализация Python-блока в RenPy
# init python:
#     # Импорт необходимых модулей
#     import random  # Для генерации случайных чисел
#     import math    # Для математических операций (хотя в текущем коде не используется)
#
#     # Конфигурация игры
# #     MAP_WIDTH = 10   # Ширина игрового поля в клетках
#     MAP_WIDTH = 32   # Ширина игрового поля в клетках
# #     MAP_HEIGHT = 15  # Высота игрового поля в клетках
#     MAP_HEIGHT = 17  # Высота игрового поля в клетках
#     CELL_SIZE = 60   # Размер одной клетки в пикселях
#     MOVE_INTERVAL = 0.5  # Интервал между движениями игрока/врагов в секундах
#
#     # Типы клеток на карте (используются для отрисовки и логики игры)
#     CELL_EMPTY = 0   # Пустая клетка
#     CELL_WALL = 1    # Стена (непроходимая)
#     CELL_PLAYER = 2  # Игрок
#     CELL_COIN = 3    # Монета (цель для сбора)
#     CELL_ENEMY = 4   # Враг (опасность)
#
#     CELL_PLAYER_TARGET = 5  # Конечная точка маршрута игрока, выводится специальный спрайт
#
#     # Стартовые параметры
#     START_NUM_COINS = 30
#     START_NUM_ENEMY = 3
#
#     # Функция инициализации игрового состояния
#     def init_game():
#         # Создаем пустую карту (двумерный список)
#         game_map = [[CELL_EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
#
#         # Создаем пустую карту (двумерный список) для отрисовки пути поверх обычной карты
#         game_map_path = [[CELL_EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
#
#         # Создаем границы карты (стены по краям)
#         for x in range(MAP_WIDTH):
#             game_map[0][x] = CELL_WALL  # Верхняя стена
#             game_map[MAP_HEIGHT-1][x] = CELL_WALL  # Нижняя стена
#         for y in range(MAP_HEIGHT):
#             game_map[y][0] = CELL_WALL  # Левая стена
#             game_map[y][MAP_WIDTH-1] = CELL_WALL  # Правая стена
#
#         # Размещаем игрока в центре карты
#         player_pos = [MAP_WIDTH // 2, MAP_HEIGHT // 2]
#         game_map[player_pos[1]][player_pos[0]] = CELL_PLAYER
#
#         # Генерируем монеты (10 штук в случайных местах)
#         coins = []
#         for _ in range(START_NUM_COINS):
#             # Генерируем случайные координаты
#             x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
#             # Убеждаемся, что клетка пуста
#             while game_map[y][x] != CELL_EMPTY:
#                 x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
#             # Размещаем монету
#             game_map[y][x] = CELL_COIN
#             coins.append((x, y))  # Добавляем в список монет
#
#         # Генерируем врагов (3 штуки в случайных местах)
#         enemies = []
#         for _ in range(START_NUM_ENEMY):
#             # Генерируем случайные координаты
#             x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
#             # Убеждаемся, что клетка пуста
#             while game_map[y][x] != CELL_EMPTY:
#                 x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
#             # Размещаем врага и задаем начальное направление движения
#             game_map[y][x] = CELL_ENEMY
#             enemies.append([x, y, random.choice([(0,1), (1,0), (0,-1), (-1,0)])])
#
#         # Возвращаем начальное состояние игры в виде словаря
#         return {
#             "map": game_map,          # Двумерный массив карты
#             "map_path": game_map_path, # Двумерный массив карты для отобажения пути игрока
#             "player_pos": player_pos, # Позиция игрока [x, y]
#             "coins": coins,          # Список позиций монет [(x1,y1), ...]
#             "enemies": enemies,       # Список врагов [[x,y, (dx,dy)], ...]
#             "score": 0,               # Счет игрока
#             "game_over": False,       # Флаг окончания игры
#             "message": "Кликните куда идти",  # Сообщение для игрока
#             "target_pos": None,       # Целевая позиция для движения
#             "path": [],              # Путь до цели (список клеток)
#             "last_move_time": 0.0,    # Время последнего движения игрока
#             "enemy_move_time": 0.0   # Время последнего движения врагов
#         }
# Инициализация Python-блока в RenPy
init python:
    # Импорт необходимых модулей
    import random  # Для генерации случайных чисел
    import math    # Для математических операций

    # Конфигурация игры
    # MAP_WIDTH = 32   # Ширина игрового поля в клетках
    # MAP_HEIGHT = 17  # Высота игрового поля в клетках

    MAP_WIDTH = 10   # Ширина игрового поля в клетках
    MAP_HEIGHT = 10  # Высота игрового поля в клетках
    CELL_SIZE = 60   # Размер одной клетки в пикселях
    MOVE_INTERVAL = 0.5  # Интервал между движениями игрока/врагов в секундах

    # Типы клеток на карте
    CELL_EMPTY = 0   # Пустая клетка
    CELL_WALL = 1    # Стена (непроходимая)
    CELL_PLAYER = 2  # Игрок
    CELL_COIN = 3    # Монета (цель для сбора)
    CELL_ENEMY = 4   # Враг (опасность)
    CELL_PLAYER_TARGET = 5  # Конечная точка маршрута игрока

    # Стартовые параметры
    START_NUM_COINS = 1
    START_NUM_ENEMY = 0
    WALL_DENSITY = 0.2  # Плотность стен (0-1), регулирует сколько стен будет сгенерировано

    # Варианты размеров карты и настроек сложности
    MAP_SIZES = {
        "small": {
            "width": 12,
            "height": 7,
            "start_enemy": 1,
            "start_coins": 5
        },
        "medium": {
            "width": 22,
            "height": 10,
            "start_enemy": 2,
            "start_coins": 10
        },
        "large": {
            "width": 32,
            "height": 15,
            "start_enemy": 3,
            "start_coins": 15
        }
    }
    # Устанавливаем размер по умолчанию
    if not hasattr(persistent, "map_size"):
        persistent.map_size = "medium"

    # Функция для генерации случайных стен на карте
    def generate_random_walls(game_map):
        """Генерирует случайные стены на карте, избегая границ и оставляя проходы.

        Args:
            game_map (list): Двумерный массив, представляющий игровую карту
        """
        # Проходим по всем клеткам карты, кроме границ
        for y in range(1, MAP_HEIGHT-1):
            for x in range(1, MAP_WIDTH-1):
                # Случайно решаем, будет ли здесь стена (с учетом плотности)
                if random.random() < WALL_DENSITY:
                    # Проверяем, что клетка пуста (не содержит игрока, монет и т.д.)
                    if game_map[y][x] == CELL_EMPTY:
                        game_map[y][x] = CELL_WALL

        # Гарантируем, что у игрока есть хотя бы один проход в каждом направлении
        center_x, center_y = MAP_WIDTH // 2, MAP_HEIGHT // 2
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Вверх, вправо, вниз, влево

        for dx, dy in directions:
            # Проверяем клетки в каждом направлении от центра
            for i in range(1, 3):  # Проверяем 2 клетки в каждом направлении
                x, y = center_x + dx*i, center_y + dy*i
                if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
                    if game_map[y][x] == CELL_WALL:
                        game_map[y][x] = CELL_EMPTY  # Удаляем стену, если она есть

    # Функция инициализации игрового состояния
    def init_game():
        # Создаем пустую карту (двумерный список)
        game_map = [[CELL_EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        # Создаем пустую карту для отрисовки пути
        game_map_path = [[CELL_EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        # Создаем границы карты (стены по краям)
        for x in range(MAP_WIDTH):
            game_map[0][x] = CELL_WALL  # Верхняя стена
            game_map[MAP_HEIGHT-1][x] = CELL_WALL  # Нижняя стена
        for y in range(MAP_HEIGHT):
            game_map[y][0] = CELL_WALL  # Левая стена
            game_map[y][MAP_WIDTH-1] = CELL_WALL  # Правая стена

        # Генерируем случайные стены внутри уровня
        generate_random_walls(game_map)

        # Размещаем игрока в центре карты
        player_pos = [MAP_WIDTH // 2, MAP_HEIGHT // 2]
        # Убеждаемся, что стартовая позиция игрока не в стене
        while game_map[player_pos[1]][player_pos[0]] != CELL_EMPTY:
            # Если центр занят, ищем ближайшую свободную клетку
            for y in range(player_pos[1]-1, player_pos[1]+2):
                for x in range(player_pos[0]-1, player_pos[0]+2):
                    if game_map[y][x] == CELL_EMPTY:
                        player_pos = [x, y]
                        break
                else:
                    continue
                break
        game_map[player_pos[1]][player_pos[0]] = CELL_PLAYER

        # Генерируем монеты (в случайных местах)
        coins = []
        for _ in range(START_NUM_COINS):
            x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            # Убеждаемся, что клетка пуста и не является стеной
            while game_map[y][x] != CELL_EMPTY:
                x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            game_map[y][x] = CELL_COIN
            coins.append((x, y))

        # Генерируем врагов (в случайных местах)
        enemies = []
        for _ in range(START_NUM_ENEMY):
            x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            # Убеждаемся, что клетка пуста и не является стеной
            while game_map[y][x] != CELL_EMPTY:
                x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            game_map[y][x] = CELL_ENEMY
            enemies.append([x, y, random.choice([(0,1), (1,0), (0,-1), (-1,0)])])

        # Возвращаем начальное состояние игры
        return {
            "map": game_map,          # Двумерный массив карты
            "map_path": game_map_path, # Карта для отображения пути
            "player_pos": player_pos, # Позиция игрока [x, y]
            "coins": coins,          # Список позиций монет
            "enemies": enemies,       # Список врагов
            "score": 0,               # Счет игрока
            "game_over": False,       # Флаг окончания игры
            "message": "Кликните куда идти",  # Сообщение
            "target_pos": None,       # Целевая позиция
            "path": [],              # Путь до цели
            "last_move_time": 0.0,    # Время последнего движения игрока
            "enemy_move_time": 0.0   # Время последнего движения врагов
        }

    # Функция проверки, можно ли переместиться в указанную клетку
    def can_move(x, y, game_state):
        # Проверка выхода за границы карты
        if x < 0 or x >= MAP_WIDTH or y < 0 or y >= MAP_HEIGHT:
            return False
        # Проверка, что клетка не является стеной
        return game_state["map"][y][x] != CELL_WALL

    # Упрощенный алгоритм поиска пути от start до end
    def find_path(start, end, game_state):
        path = []
        sx, sy = start  # Стартовая позиция
        ex, ey = end    # Конечная позиция

        # Определяем направление движения по X
        dx = 1 if ex > sx else -1
        # Определяем направление движения по Y
        dy = 1 if ey > sy else -1

        # Двигаемся сначала по горизонтали (X)
        x = sx
        while x != ex:
            x += dx
            # Если на пути стена - прерываем движение
            if not can_move(x, sy, game_state):
                break
            path.append((x, sy))  # Добавляем клетку в путь

        # Затем двигаемся по вертикали (Y)
        y = sy
        while y != ey:
            y += dy
            # Если на пути стена - прерываем движение
            if not can_move(ex, y, game_state):
                break
            path.append((ex, y))  # Добавляем клетку в путь

        # Возвращаем путь только если достигли конечной точки
        return path if path and path[-1] == (ex, ey) else []

    # Обработчик клика по карте
    def handle_click(pos):
        # Если игра окончена, клик перезапускает игру
        if game_state["game_over"]:
            restart_game()
            return

        # Преобразуем координаты клика в клетку карты
        tx = int(pos[0] / CELL_SIZE)
        ty = int(pos[1] / CELL_SIZE)
        px, py = game_state["player_pos"]  # Текущая позиция игрока

        # Если кликнули на текущую позицию игрока - ничего не делаем
        if (tx, ty) == (px, py):
            return

        # Проверяем, можно ли переместиться в выбранную клетку
        if not can_move(tx, ty, game_state):
            game_state["message"] = "Нельзя идти в стену!"
            return

        # Сначала очистим старую точку в карте маршрута
        game_state["map_path"][ty][tx] = CELL_EMPTY
        print(game_state["target_pos"])

        # Теперь устанавливаем новую цель для движения
        game_state["target_pos"] = (tx, ty)
        game_state["map_path"][ty][tx] = CELL_PLAYER_TARGET
        print(game_state["target_pos"])

#         print(f"Конечная точка пути игрока. {game_state['map_path'][tx][ty]}")
#         print(ty, tx)
#         print(game_state["map_path"])
#         print(game_state["map"])

        # Находим путь до цели
        game_state["path"] = find_path((px, py), (tx, ty), game_state)

        # Если путь не найден
        if not game_state["path"]:
            game_state["message"] = "Нет пути к цели!"
            game_state["target_pos"] = None  # Сбрасываем цель
        else:
            game_state["message"] = f"Иду к ({tx}, {ty})"

    # Обработчик нажатий клавиш
    def handle_key(key):
        # Если игра окончена, любая клавиша перезапускает игру
        if game_state["game_over"]:
            restart_game()
            return

        px, py = game_state["player_pos"]  # Текущая позиция игрока
        dx, dy = 0, 0  # Направление движения

        # Определяем направление по нажатой клавише
        if key in ('K_UP', 'w'):    # Стрелка вверх или W
            dy = -1
        elif key in ('K_DOWN', 's'): # Стрелка вниз или S
            dy = 1
        elif key in ('K_LEFT', 'a'): # Стрелка влево или A
            dx = -1
        elif key in ('K_RIGHT', 'd'): # Стрелка вправо или D
            dx = 1
        else:
            return  # Игнорируем другие клавиши

        # Вычисляем новую позицию
        tx, ty = px + dx, py + dy

        # Проверяем, можно ли переместиться в выбранную клетку
        if not can_move(tx, ty, game_state):
            game_state["message"] = "Нельзя идти в стену!"
            return

        # Очищаем старую цель и путь
        if game_state["target_pos"]:
            old_tx, old_ty = game_state["target_pos"]
            game_state["map_path"][old_ty][old_tx] = CELL_EMPTY
        game_state["path"] = []

        # Устанавливаем новую цель - следующую клетку в направлении движения
        game_state["target_pos"] = (tx, ty)
        game_state["map_path"][ty][tx] = CELL_PLAYER_TARGET
        game_state["path"] = [(tx, ty)]  # Путь состоит только из одной клетки
        game_state["message"] = f"Иду к ({tx}, {ty})"


    # Функция движения игрока по найденному пути
    def move_player(game_state):
        # Если игра окончена или путь пуст - ничего не делаем
        if game_state["game_over"] or not game_state["path"]:
            return False

        # Берем следующую клетку из пути
        next_x, next_y = game_state["path"].pop(0)
        px, py = game_state["player_pos"]  # Текущая позиция

        # Проверяем, что находится в следующей клетке
        cell = game_state["map"][next_y][next_x]

        # Если в клетке монета
        if cell == CELL_COIN:
            game_state["score"] += 1  # Увеличиваем счет
            game_state["coins"].remove((next_x, next_y))  # Удаляем монету из списка
            game_state["message"] = f"Монета! Счёт: {game_state['score']}"
        # Если в клетке враг - игра окончена
        elif cell == CELL_ENEMY:
            game_state["game_over"] = True
            game_state["message"] = "Поражение! Кликните для рестарта"
            game_state["path"] = []  # Очищаем путь
            return False

        # Перемещаем игрока
        game_state["map"][py][px] = CELL_EMPTY  # Освобождаем старую клетку
        game_state["map"][next_y][next_x] = CELL_PLAYER  # Занимаем новую
        game_state["player_pos"] = [next_x, next_y]  # Обновляем позицию

        # Если достигли цели
        if not game_state["path"] and game_state["target_pos"] == (next_x, next_y):
            game_state["message"] = "Цель достигнута!"
            game_state["target_pos"] = None  # Сбрасываем цель

        return True  # Движение успешно

    # Функция движения врагов
    def move_enemies(game_state):
        for enemy in game_state["enemies"]:
            x, y, (dx, dy) = enemy  # Текущая позиция и направление

            # С вероятностью 30% меняем направление движения
            if random.random() < 0.3:
                directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Все возможные направления
                random.shuffle(directions)  # Перемешиваем
                dx, dy = directions[0]  # Выбираем первое направление
                enemy[2] = (dx, dy)  # Обновляем направление врага

            # Вычисляем новую позицию
            nx, ny = x + dx, y + dy

            # Если в новую позицию нельзя переместиться
            if not can_move(nx, ny, game_state) or game_state["map"][ny][nx] not in (CELL_EMPTY, CELL_PLAYER, CELL_COIN):
                # Пробуем найти новое направление
                directions = [(0,1), (1,0), (0,-1), (-1,0)]
                random.shuffle(directions)
                for ndx, ndy in directions:
                    if can_move(x + ndx, y + ndy, game_state):
                        dx, dy = ndx, ndy
                        enemy[2] = (dx, dy)  # Обновляем направление
                        nx, ny = x + dx, y + dy
                        break
                else:
                    continue  # Если не нашли подходящее направление - пропускаем ход

            # Если враг достиг игрока - игра окончена
            if game_state["map"][ny][nx] == CELL_PLAYER:
                game_state["game_over"] = True
                game_state["message"] = "Враг догнал вас!"

            # Перемещаем врага
            game_state["map"][y][x] = CELL_EMPTY  # Освобождаем старую позицию
            enemy[0], enemy[1] = nx, ny  # Обновляем координаты врага

            # Если враг наступил на монету - удаляем монету
            if (nx, ny) in game_state["coins"]:
                game_state["coins"].remove((nx, ny))

            # Занимаем новую клетку
            game_state["map"][ny][nx] = CELL_ENEMY

    # Функция обновления игрового состояния
    def game_update():
        # Проверка на количество монет. TODO делать в начале или в конце функции?
        if len(game_state['coins']) <= 0:  # Если монеток не осталось
            renpy.show_screen("victory_screen")

        # Если игра окончена - ничего не обновляем
        if game_state["game_over"]:
            return

        current_time = renpy.get_game_runtime()  # Текущее игровое время

        # Проверяем, нужно ли двигать игрока
        if current_time - game_state["last_move_time"] >= MOVE_INTERVAL:
            if move_player(game_state):
                game_state["last_move_time"] = current_time  # Обновляем время последнего хода

        # Проверяем, нужно ли двигать врагов
        if current_time - game_state["enemy_move_time"] >= MOVE_INTERVAL:
            move_enemies(game_state)
            game_state["enemy_move_time"] = current_time  # Обновляем время последнего хода врагов

        renpy.restart_interaction()  # Обновляем экран

    # Функция перезапуска игры
    def restart_game():
        global game_state
        game_state = init_game()  # Инициализируем новое состояние
        renpy.restart_interaction()  # Обновляем экран

    # Функция перезапуска игры
    def new_game():
        global game_state
        game_state = init_game()  # Инициализируем новое состояние
        renpy.restart_interaction()  # Обновляем экран


# Экран игры (интерфейс)
screen game_screen():
    # Обработчики нажатия клавиш
    key "K_UP" action Function(handle_key, "K_UP")  # Стрелка вверх
    key "K_DOWN" action Function(handle_key, "K_DOWN")  # Стрелка вниз
    key "K_LEFT" action Function(handle_key, "K_LEFT")  # Стрелка влево
    key "K_RIGHT" action Function(handle_key, "K_RIGHT")  # Стрелка вправо
    key "w" action Function(handle_key, "w")  # Клавиша W
    key "a" action Function(handle_key, "a")  # Клавиша A
    key "s" action Function(handle_key, "s")  # Клавиша S
    key "d" action Function(handle_key, "d")  # Клавиша D

    # Создаем сетку клеток (игровое поле)
    grid MAP_WIDTH MAP_HEIGHT:
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                $ cell = game_state["map"][y][x]  # Получаем тип клетки
                $ cell_path = game_state["map_path"][y][x]  # Получаем тип клетки для вывода пути
                button:
                    xsize CELL_SIZE  # Ширина кнопки = размеру клетки
                    ysize CELL_SIZE  # Высота кнопки = размеру клетки
                    # При клике вызываем обработчик с координатами
                    action Function(handle_click, (x * CELL_SIZE + CELL_SIZE/2, y * CELL_SIZE + CELL_SIZE/2))

                    # Отрисовываем содержимое клетки в зависимости от типа
                    if cell == CELL_EMPTY:
                        text " "  # Пустая клетка
                    elif cell == CELL_WALL:
                        add "wall.jpg"
                    elif cell == CELL_PLAYER:
                        add "0_Minotaur_Running_000_100.png"
                    elif cell == CELL_COIN:
                        add "23.png"
                    elif cell == CELL_ENEMY:
                        add "0_Skeleton_Warrior_Running_000_free.png" fit "contain"

#                     if cell_path == CELL_PLAYER_TARGET:
#                         add "wall.jpg"

    # Контейнер для интерфейса. vbox - вертикальный, hbox - горизонтальный.
    hbox:
        xalign 0.5  # Выравнивание по центру по X
        ypos 20    # Позиция по Y
        spacing 20  # Расстояние между элементами внутри hbox
        text "Roguelike на RenPy." size 30 xalign 0.1 # color # "#000000" # Заголовок
        text "Счёт: [game_state['score']]" size 30 xalign 1  # Отображение счета

        # Скроем вывод пути, пока не решили вопрос построения пути с учетом стен
#         text "[game_state['message']]" size 20 xalign 0.5  # Сообщение игроку
        # Если есть цель - показываем ее координаты
#         if game_state["target_pos"]:
#             $ tx, ty = game_state["target_pos"]
#             text f"Цель: ({tx}, {ty})" size 16 xalign 0.5

    # Кнопка рестарта
    frame:
        xalign 0.5  # По центру по X
        yanchor 1.0  # Привязка к нижнему краю
        ypos 0.95     # В самом низу
        textbutton "Рестарт":
            action Function(restart_game)  # При клике перезапускаем игру

#     # Кнопка начала новой игры(обучение + выбор размера карты)
#     frame:
#         xalign 0.5  # По центру по X
#         yanchor 1.0  # Привязка к нижнему краю
#         ypos 0.95     # В самом низу
#         textbutton "Рестарт":
#             action Function(restart_game)  # При клике перезапускаем игру

    # Таймер для обновления игры (вызывается каждые 0.1 секунды)
    timer 0.1 repeat True action Function(game_update)

# # Основная сцена игры (Без обучения)
# label start:
#     $ game_state = init_game()  # Инициализируем состояние игры
#     show screen game_screen    # Показываем игровой экран
#
#     # Бесконечный цикл (игра управляется через экран и обработчики)
#     while True:
#         pause 1.0  # Пауза для предотвращения 100% загрузки CPU


# Основная сцена игры
label start:
    if persistent.map_size not in MAP_SIZES:
        $ persistent.map_size = "medium"

    $ current_size = MAP_SIZES[persistent.map_size]
    $ MAP_WIDTH = current_size["width"]
    $ MAP_HEIGHT = current_size["height"]
    $ START_NUM_ENEMY = current_size["start_enemy"]
    $ START_NUM_COINS = current_size["start_coins"]

#     # Устанавливаем размер карты из сохраненного значения
#     $ MAP_WIDTH = MAP_SIZES[persistent.map_size]["width"]
#     $ MAP_HEIGHT = MAP_SIZES[persistent.map_size]["height"]
#
#     $ START_NUM_ENEMY = START_NUM_ENEMY[persistent.map_size]["start_enemy"]
#     $ START_NUM_COINS = START_NUM_COINS[persistent.map_size]["start_coins"]

    # Показываем экран обучения перед началом игры
    call screen tutorial_screen

    # Инициализируем состояние игры
    $ game_state = init_game()

    # Показываем игровой экран
    show screen game_screen

    # Бесконечный цикл (игра управляется через экран и обработчики)
    while True:
        pause 1.0  # Пауза для предотвращения 100% загрузки CPU
