init python:
    import random
    import math

    # Конфигурация игры
    MAP_WIDTH = 35
    MAP_HEIGHT = 20
    CELL_SIZE = 50
    MOVE_INTERVAL = 0.5  # Интервал движения в секундах

    # Типы клеток
    CELL_EMPTY = 0
    CELL_WALL = 1
    CELL_PLAYER = 2
    CELL_COIN = 3
    CELL_ENEMY = 4

    # Инициализация игры
    def init_game():
        game_map = [[CELL_EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        # Границы карты
        for x in range(MAP_WIDTH):
            game_map[0][x] = CELL_WALL
            game_map[MAP_HEIGHT-1][x] = CELL_WALL
        for y in range(MAP_HEIGHT):
            game_map[y][0] = CELL_WALL
            game_map[y][MAP_WIDTH-1] = CELL_WALL

        # Игрок
        player_pos = [MAP_WIDTH // 2, MAP_HEIGHT // 2]
        game_map[player_pos[1]][player_pos[0]] = CELL_PLAYER

        # Монеты
        coins = []
        for _ in range(10):
            x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            while game_map[y][x] != CELL_EMPTY:
                x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            game_map[y][x] = CELL_COIN
            coins.append((x, y))

        # Враги
        enemies = []
        for _ in range(3):
            x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            while game_map[y][x] != CELL_EMPTY:
                x, y = random.randint(1, MAP_WIDTH-2), random.randint(1, MAP_HEIGHT-2)
            game_map[y][x] = CELL_ENEMY
            enemies.append([x, y, random.choice([(0,1), (1,0), (0,-1), (-1,0)])])

        return {
            "map": game_map,
            "player_pos": player_pos,
            "coins": coins,
            "enemies": enemies,
            "score": 0,
            "game_over": False,
            "message": "Кликните куда идти",
            "target_pos": None,  # Новая цель для движения
            "path": [],  # Путь до цели
            "last_move_time": 0.0,
            "enemy_move_time": 0.0
        }

    # Проверка доступности клетки
    def can_move(x, y, game_state):
        if x < 0 or x >= MAP_WIDTH or y < 0 or y >= MAP_HEIGHT:
            return False
        return game_state["map"][y][x] != CELL_WALL

    # Поиск пути (упрощенный)
    def find_path(start, end, game_state):
        path = []
        sx, sy = start
        ex, ey = end

        # Простой алгоритм - сначала по X, потом по Y
        dx = 1 if ex > sx else -1
        dy = 1 if ey > sy else -1

        # Двигаемся по X
        x = sx
        while x != ex:
            x += dx
            if not can_move(x, sy, game_state):
                break
            path.append((x, sy))

        # Двигаемся по Y
        y = sy
        while y != ey:
            y += dy
            if not can_move(ex, y, game_state):
                break
            path.append((ex, y))

        return path if path and path[-1] == (ex, ey) else []

    # Обработка клика
    def handle_click(pos):
        if game_state["game_over"]:
            restart_game()
            return

        tx = int(pos[0] / CELL_SIZE)
        ty = int(pos[1] / CELL_SIZE)
        px, py = game_state["player_pos"]

        if (tx, ty) == (px, py):
            return

        if not can_move(tx, ty, game_state):
            game_state["message"] = "Нельзя идти в стену!"
            return

        game_state["target_pos"] = (tx, ty)
        game_state["path"] = find_path((px, py), (tx, ty), game_state)

        if not game_state["path"]:
            game_state["message"] = "Нет пути к цели!"
            game_state["target_pos"] = None
        else:
            game_state["message"] = f"Иду к ({tx}, {ty})"

    # Движение игрока по пути
    def move_player(game_state):
        if game_state["game_over"] or not game_state["path"]:
            return False

        next_x, next_y = game_state["path"].pop(0)
        px, py = game_state["player_pos"]

        cell = game_state["map"][next_y][next_x]

        if cell == CELL_COIN:
            game_state["score"] += 1
            game_state["coins"].remove((next_x, next_y))
            game_state["message"] = f"Монета! Счёт: {game_state['score']}"
        elif cell == CELL_ENEMY:
            game_state["game_over"] = True
            game_state["message"] = "Поражение! Кликните для рестарта"
            game_state["path"] = []
            return False

        game_state["map"][py][px] = CELL_EMPTY
        game_state["map"][next_y][next_x] = CELL_PLAYER
        game_state["player_pos"] = [next_x, next_y]

        # Если достигли цели
        if not game_state["path"] and game_state["target_pos"] == (next_x, next_y):
            game_state["message"] = "Цель достигнута!"
            game_state["target_pos"] = None

        return True

    # Движение врагов
    def move_enemies(game_state):
        for enemy in game_state["enemies"]:
            x, y, (dx, dy) = enemy

            if random.random() < 0.3:
                directions = [(0,1), (1,0), (0,-1), (-1,0)]
                random.shuffle(directions)
                dx, dy = directions[0]
                enemy[2] = (dx, dy)

            nx, ny = x + dx, y + dy

            if not can_move(nx, ny, game_state) or game_state["map"][ny][nx] not in (CELL_EMPTY, CELL_PLAYER, CELL_COIN):
                directions = [(0,1), (1,0), (0,-1), (-1,0)]
                random.shuffle(directions)
                for ndx, ndy in directions:
                    if can_move(x + ndx, y + ndy, game_state):
                        dx, dy = ndx, ndy
                        enemy[2] = (dx, dy)
                        nx, ny = x + dx, y + dy
                        break
                else:
                    continue

            if game_state["map"][ny][nx] == CELL_PLAYER:
                game_state["game_over"] = True
                game_state["message"] = "Враг догнал вас!"

            game_state["map"][y][x] = CELL_EMPTY
            enemy[0], enemy[1] = nx, ny

            if (nx, ny) in game_state["coins"]:
                game_state["coins"].remove((nx, ny))

            game_state["map"][ny][nx] = CELL_ENEMY

    # Обновление игры
    def game_update():
        if game_state["game_over"]:
            return

        current_time = renpy.get_game_runtime()

        if current_time - game_state["last_move_time"] >= MOVE_INTERVAL:
            if move_player(game_state):
                game_state["last_move_time"] = current_time

        if current_time - game_state["enemy_move_time"] >= MOVE_INTERVAL:
            move_enemies(game_state)
            game_state["enemy_move_time"] = current_time

        renpy.restart_interaction()

    # Рестарт игры
    def restart_game():
        global game_state
        game_state = init_game()
        renpy.restart_interaction()

# Экран игры
screen game_screen():
    grid MAP_WIDTH MAP_HEIGHT:
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                $ cell = game_state["map"][y][x]
                button:
                    xsize CELL_SIZE
                    ysize CELL_SIZE
                    action Function(handle_click, (x * CELL_SIZE + CELL_SIZE/2, y * CELL_SIZE + CELL_SIZE/2))
                    if cell == CELL_EMPTY:
                        text " "
                    elif cell == CELL_WALL:
                        text "#" color "#888"
                    elif cell == CELL_PLAYER:
                        text "@" color "#0f0"
                    elif cell == CELL_COIN:
                        text "$" color "#ff0"
                    elif cell == CELL_ENEMY:
                        text "E" color "#f00"

    vbox:
        xalign 0.5
        ypos 20
        text "Roguelike с путём" size 30 xalign 0.5
        text "Счёт: [game_state['score']]" size 24 xalign 0.5
        text "[game_state['message']]" size 20 xalign 0.5
        if game_state["target_pos"]:
            $ tx, ty = game_state["target_pos"]
            text f"Цель: ({tx}, {ty})" size 16 xalign 0.5

    frame:
        xalign 0.5
        yanchor 1.0
        ypos 1.0
        textbutton "Рестарт":
            action Function(restart_game)

    timer 0.1 repeat True action Function(game_update)

# Основная сцена
label start:
    $ game_state = init_game()
    show screen game_screen

    while True:
        pause 1.0