import pygame
pygame.init()
win = pygame.display.set_mode((850,480))

pygame.display.set_caption("hello there ")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock=pygame.time.Clock()

class player(object):
    def __init__(self,x,y,height,width):
        self.x= x
        self.y=y
        self.height=height
        self.width=width
        self.vel=10
        self.isJump=False
        self.jumpCount=10
        self.Left=False
        self.Right=False
        self.Walk=0
        self.standing = True

    def draw(self,win):
        if self.Walk + 1 >= 27:
            self.Walk = 0

        if not(self.standing):
            if self.Left:
                win.blit(walkLeft[self.Walk // 3], (self.x, self.y))
                self.Walk += 1

            elif self.Right:
                win.blit(walkRight[self.Walk // 3], (self.x, self.y))
                self.Walk += 1
        else:
            if self.Right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius )





def redrawGameWindow():

    win.blit(bg,(0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

#main loop
man = player(50,380,64,64)
run = True
bullets = []
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
    for bullet in bullets:
        if bullet.x < 850 and bullet.x>0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.Left:
            facing= -1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x + man.width//2),round(man.y , man.height//2),6,(0,0,0),facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.Left= True
        man.Right=False
        man.standing=False

    elif keys[pygame.K_RIGHT] and man.x < 800:
        man.x += man.vel
        man.Right=True
        man.Left=False
        man.standing=False
    else:
        man.standing=True
        man.Walk=0
    if not(man.isJump):

        if keys[pygame.K_UP] :
            man.isJump = True
            man.Right=False
            man.Left=False
            man.Walk=0

    else :
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount<0:
                neg= -1
            man.y -= (man.jumpCount ** 2)* 0.5 * neg
            man.jumpCount -= 1
        else :
            man.isJump =False
            man.jumpCount=10

    redrawGameWindow()



pygame.quit
