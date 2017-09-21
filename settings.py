shadow_mode = True
window_mode = 1
revert = False

visible_background_color = 'white'
invisible_background_color = 'lightblue'

visible_color = 'red'
visible_border_color = ''

invisible_color = ''
invisible_border_color = 'gray'

if revert:
    visible_background_color, invisible_background_color = invisible_background_color, visible_background_color
    invisible_color = visible_color
    visible_color = visible_background_color
