from window import *

width = 600
height = 600
window = pygame.display.set_mode((width, height))  # main window of game

display = Window(width, height, window)
display.start_window()