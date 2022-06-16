import pygame, sys

pygame.init()
pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Chinezelum Okadigbo')
            pygame.quit()
            sys.exit()
    pygame.display.update()