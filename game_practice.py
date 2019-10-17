import pygame
pygame.init()
#every time use this upper line to initial pygame

win = pygame.display.set_mode((500,500))
#this upper line makes window to play game in , here "win" is variable for that window

pygame.display.set_caption("my first pygame")

x=50
y=400
height=40
width= 40
vel = 5

isJump= True
jumpCount = 10
jumpHeight = 50

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and x < 450:
        x += vel
    if keys[pygame.K_a] and x > vel:
        x -= vel
    if not(isJump):
`            y += vel
        if keys[pygame.K_w] and y > vel:
            y -= vel
        if keys[pygame.K_SPACE] :
            isJump= True
    else:
        if jumpCount >= -10:
            heg=1
            if jumpCount<0:
                heg= -1
            y -= (jumpCount ** 2)* 0.5 * heg
            jumpCount -= 1
        else :
            isJump = False
            jumpCount=10

    win.fill((0,0,0))
    pygame.draw.rect(win, (253,52,1), (x,y,height,width))
    pygame.display.update()

pygame.quit()
