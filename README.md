# Algorithms of machine graphics

## Description

Implementation polygon-clipping with Cohen–Sutherland and Cyrus–Beck algorithms.

Random polygon move from left-top to right-bottom corner with morphing. 
If window exists, polygon is visible only inside the window.
Optional tracking.

## Launch

`python main.py <window_mode> <tracking_mode>`

* window_mode: 
    * `0` - no window
    * `1` - cross window
    * `2` - complex 3-triangle window

* tracking_mode:
    * `0` - tracking off
    * `1` - tracking on