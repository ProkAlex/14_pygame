import pygame
import sys

pygame.init()

W = 500
H = 500

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RANDOMCOLOR = (222, 145, 86)

window = pygame.display.set_caption("Hello Pygame")
window = pygame.display.set_icon(pygame.image.load("cat3.png"))
window = pygame.display.set_mode((W, H))

fps = 60
clock = pygame.time.Clock()

# window.fill((255, 255, 255))

pygame.display.update()
'''
#rect
pygame.draw.rect(window, (255, 0, 0), (30, 30, 100, 50))
pygame.draw.rect(window, RANDOMCOLOR, (50, 130, 100, 100), 5)
#line
pygame.draw.line(window, RED, [50, 50], [300, 100], 3)
pygame.draw.aaline(window, BLUE, [100, 100], [300, 300], 2)
#poly
pygame.draw.polygon(window, GREEN, [[250, 100],
[280, 150], [200, 200], [140, 140]])
#circle
pygame.draw.circle(window, RED, (400, 400), 50, 10)
'''
circle_x = 50
circle_y = 50

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        '''
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                circle_x += 10
            if event.key == pygame.K_LEFT:
                circle_x -= 10
        '''
        #
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('1')
            elif event.button == 2:
                print('2')
            elif event.button == 3:
                print('3')
        '''
    #window.fill((255, 255, 255))
    # pygame.draw.circle(window, RED, (circle_x, circle_y), 10, 2)

    #if circle_x - 490:
    # if circle_x <= 490:
    #     circle_x += 1
    #circle_y += 1
    '''
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        circle_x += 5
    elif key[pygame.K_LEFT]:
        circle_x -= 5
    '''
    pre = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if pre[0]:
        pygame.draw.circle(window, RED, pos, 5)
        pygame.display.update()

    pygame.display.update()