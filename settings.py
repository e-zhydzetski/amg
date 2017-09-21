shadow_mode = False  # Режим следа
window_mode = 1  # Режим окна: 0 - без окна, 1 - крест, 2 - пирамида из треугольников
revert = True  # Эмулировать внешнее отсечение (для режима с окном)

visible_background_color = 'white'  # Цвет фона
invisible_background_color = 'lightblue'  # Цвет окна за которым не видно фигуру

visible_color = 'red'  # Цвет заливки видимой части фигуры
visible_border_color = ''  # Цвет границы видимой части фигуры (для режима с окном)

invisible_color = ''  # Цвет заливки невидимой части фигуры
invisible_border_color = 'gray'  # Цвет границы невидимой части фигуры (для режима с окном)


# Если нет окна - рисовать границу для видимого объекта
if not window_mode:
    visible_border_color = invisible_border_color
else:
    if revert:  # хитрый финт с цветами для эмуляции обратног отсечения
        visible_background_color, invisible_background_color = invisible_background_color, visible_background_color
        invisible_color = visible_color
        visible_color = visible_background_color
