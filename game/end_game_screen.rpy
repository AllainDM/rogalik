screen victory_screen():
    # Затемнение фона
    add Solid("#000000AA")  # Полупрозрачный чёрный

    # Основное окно победы
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 30
        background "#333333"  # Тёмный фон окна

        vbox:
            spacing 20
            align (0.5, 0.5)

            # Заголовок
            text "ПОБЕДА!":
                size 40
                color "#FFD700"  # Золотой цвет
                bold True
                xalign 0.5

#             # Статистика
#             text f"Собрано монет: {game_state['total_coins'] - game_state['coins_left']}/{game_state['total_coins']}":
#                 size 28
#                 color "#FFFFFF"
#                 xalign 0.5
#
#             text f"Потрачено ходов: {game_state['moves']}":
#                 size 28
#                 color "#FFFFFF"
#                 xalign 0.5

            # Кнопка "Заново"
            textbutton "Играть заново":
                xalign 0.5
                action [Hide("victory_screen"), Function(restart_game)]  # Закрывает экран и перезапускает игру
                background "#4CAF50"  # Зелёный
                hover_background "#2E7D32"
                text_color "#FFFFFF"
                padding (25, 10)
