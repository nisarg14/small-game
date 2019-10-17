import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("my first pygame project")

x=50
y=50
height=40
width=60
vel=5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed( )

    if keys[pygame.K_w]:
        x += vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (253,52,1), (x,y,height,width))
    pygame.display.update()
pygame.quit