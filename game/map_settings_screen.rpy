screen map_size_selector():
    zorder 100

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Выберите размер карты:":
            size 28
            xalign 0.5

        hbox:
            spacing 40
            xalign 0.5

            # Маленькая карта
            textbutton "Маленькая (12x7)":
                action [
                    SetVariable("MAP_WIDTH", MAP_SIZES["small"]["width"]),
                    SetVariable("MAP_HEIGHT", MAP_SIZES["small"]["height"]),
                    SetVariable("START_NUM_ENEMY", MAP_SIZES["small"]["start_enemy"]),
                    SetVariable("START_NUM_COINS", MAP_SIZES["small"]["start_coins"]),
                    SetField(persistent, "map_size", "small")
                ]
                selected (persistent.map_size == "small")
                style "map_size_button"

            # Средняя карта
            textbutton "Средняя (22x10)":
                action [
                    SetVariable("MAP_WIDTH", MAP_SIZES["medium"]["width"]),
                    SetVariable("MAP_HEIGHT", MAP_SIZES["medium"]["height"]),
                    SetVariable("START_NUM_ENEMY", MAP_SIZES["medium"]["start_enemy"]),
                    SetVariable("START_NUM_COINS", MAP_SIZES["medium"]["start_coins"]),
                    SetField(persistent, "map_size", "medium")
                ]
                selected (persistent.map_size == "medium")
                style "map_size_button"

            # Большая карта
            textbutton "Большая (32x15)":
                action [
                    SetVariable("MAP_WIDTH", MAP_SIZES["large"]["width"]),
                    SetVariable("MAP_HEIGHT", MAP_SIZES["large"]["height"]),
                    SetVariable("START_NUM_ENEMY", MAP_SIZES["large"]["start_enemy"]),
                    SetVariable("START_NUM_COINS", MAP_SIZES["large"]["start_coins"]),
                    SetField(persistent, "map_size", "large")
                ]
                selected (persistent.map_size == "large")
                style "map_size_button"

# Стиль для кнопок выбора размера
style map_size_button:
    background "#333"
    hover_background "#555"
    selected_background "#0077CC"
    padding (25, 15)
    xminimum 150