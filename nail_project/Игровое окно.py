import pygame

pygame.init()

size = (600, 400)
RED= (255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK= (0,0,0)
x,y = 0,300
FPS= 2000
direct_x=1
direct_y=1

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('comicsansms',32)
image=pygame.image.load("snake.png")
pygame.display.set_icon(image)
pygame.display.set_caption("Snake the game")

follow = font.render("Hello, Brat ",1,GREEN,BLACK)
e,g = follow.get_size()
like = font.render("Your life",1,RED,BLUE)
w,h  = like.get_size()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        clock.tick(FPS)
        screen.fill(BLACK)
        screen.blit(follow, ((600-e)//2,(400-g)//2))
        screen.blit(like, (x,y))
        x+=direct_x
        if x+w>=600 or x<0:
            direct_x=-direct_x
        y += direct_y
        if y + h >= 400 or y < 0:
            direct_y = -direct_y
        pygame.display.update()





