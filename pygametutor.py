import pygame

width = 500
height = 500
window = pygame.display.set_mode((width, height))  # окно самого pygame
pygame.init()  # инициализация библиотеки
pygame.display.set_caption("Name of game")  # название игры на окне
icon = pygame.image.load("a2f3b680ae0498546d10a563c4a1e18d.png") #загрузка лого игры
pygame.display.set_icon(icon) #отображение лого игры

def run_game():
    while True:
        for event in pygame.event.get():  # проверка действий в pygame
            if event.type == pygame.QUIT:  # если нажата кнопка X (quit)
                pygame.quit()
                quit()
        window.fill(pygame.Color("red"))  # заполнение всего окна красным цветом
        pygame.display.update()  # обновление дисплея


run_game()
