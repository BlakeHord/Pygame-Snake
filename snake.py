import pygame
import sys

class snake:
    def __init__(self):
        self.x = 25
        self.y = 25
        self.length = 1
        self.speed = [1,0]

    def draw(self, screen, rect):
        pygame.draw.rect(screen, red, rect)

class lines:
    def __init__(self):
        self.num = 49

    def draw(self, screen):
        for i in range(1,self.num + 1):
            pygame.draw.line(screen, black, [0,10*i], [500,10*i])
            pygame.draw.line(screen, black, [10*i,0], [10*i,500])
        
grid = [[0] * 50] * 50
        
size = width, height = 500, 500
white = 255, 255, 255
black = 0,0,0
red = 255,0,0

screen = pygame.display.set_mode(size)

rect = [0,0,10,10]

grid = lines()
player = snake()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        
    screen.fill(white)
    player.draw(screen,rect)
    grid.draw(screen)
    pygame.display.flip()

    rect[0] += 10
    rect[1] += 10
    
    while 1:
        a=0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    a=1
            elif event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        if a==1:
            break

