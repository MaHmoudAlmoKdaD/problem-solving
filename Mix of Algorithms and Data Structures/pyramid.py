def draw_pyramid(height):
    for level in range(1, height + 1):
        spaces = height - level
        print(' ' * spaces, end='')
        print('#' * level, ' ', end='')
        print('#' * level,' ' * spaces)
draw_pyramid(5)
