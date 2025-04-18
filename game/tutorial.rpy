# Экран обучения (появляется перед началом игры)
screen tutorial_screen():
    zorder 200
    # Фон для экрана обучения
    frame:
        xfill True
        yfill True
        background "#333333"  # Полупрозрачный темный фон
#         background "#333333cc"  # Полупрозрачный темный фон

        # Основной контейнер с содержимым обучения
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            # Заголовок обучения
            label "Обучение":
                xalign 0.5
                text_size 40
                text_color "#FFFFFF"

            # Горизонтальный блок с описанием игрока
            hbox:
                spacing 20
                xalign 0.5
                # Спрайт игрока
                add "0_Minotaur_Running_000_100.png":
                    zoom 1.5  # Уменьшаем спрайт для обучения
                # Описание игрока
                vbox:
                    spacing 5
                    text "Игрок" size 30 color "#FFFFFF"
                    text "Это ваш персонаж, которым вы управляете." size 24 color "#CCCCCC"

            # Горизонтальный блок с описанием врагов
            hbox:
                spacing 20
                xalign 0.5
                # Спрайт врага
                add "0_Skeleton_Warrior_Running_000_free.png":
                    zoom 0.1
                    fit "contain"
                # Описание врагов
                vbox:
                    spacing 5
                    text "Враги" size 30 color "#FF5555"
                    text "Избегайте врагов, они опасны!" size 24 color "#CCCCCC"

            # Горизонтальный блок с описанием монет
            hbox:
                spacing 20
                xalign 0.5
                # Спрайт монеты
                add "23.png":
                    zoom 1.5
                # Описание монет
                vbox:
                    spacing 5
                    text "Золото" size 30 color "#FFD700"
                    text "Собирайте золото для увеличения счета." size 24 color "#CCCCCC"

            # Блок с управлением
            frame:
                xalign 0.5
                xpadding 20
                ypadding 20
                background "#444444"

                vbox:
                    spacing 10
                    label "Управление(зажатие клавиш не работает).":
                        xalign 0.5
                        text_size 30
                        text_color "#FFFFFF"

                    # Таблица с управлением
                    grid 2 4:
                        xalign 0.5
                        spacing 10

                        text "Движение вверх:" size 24 color "#FFFFFF"
                        text "Стрелка вверх или W" size 24 color "#AAAAFF"

                        text "Движение вниз:" size 24 color "#FFFFFF"
                        text "Стрелка вниз или S" size 24 color "#AAAAFF"

                        text "Движение влево:" size 24 color "#FFFFFF"
                        text "Стрелка влево или A" size 24 color "#AAAAFF"

                        text "Движение вправо:" size 24 color "#FFFFFF"
                        text "Стрелка вправо или D" size 24 color "#AAAAFF"

            # Кнопка для начала игры
            textbutton "Начать игру":
                xalign 0.5
                # action [Hide("tutorial_screen"), Return("start_game")]
                # action [Hide("tutorial_screen"), Return("restart")]
                # action [Hide("tutorial_screen"), Return()]  # Скрываем экран и возвращаемся

                action Return()

                background "#5555FF"
                hover_background "#7777FF"
                text_color "#FFFFFF"
                text_hover_color "#FFFFFF"
                padding (25, 10)

            # Добавляем выбор размера карты
            if renpy.has_screen("map_size_selector"):
                use map_size_selector
            else:
                text "Ошибка загрузки настроек карты" color "#FF0000"