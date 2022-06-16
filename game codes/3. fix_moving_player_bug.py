import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
BACKGROUND_COLOR = (0,0,0)
player_pos = [400,300]
player_size = 50

screen = pygame.display.set_mode((WIDTH,HEIGHT))

not_game_over = True

while not_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x = x- player_size
            elif event.key == pygame.K_RIGHT:
                x = x + player_size
            #I added this for it to move up and down :) ;)
            elif event.key == pygame.K_UP:
                y = y - player_size
            elif event.key == pygame.K_DOWN:
                y = y + player_size
            player_pos = [x,y]
    screen.fill(BACKGROUND_COLOR) # this resets the screen, fixing the error and allowing the new box to show in its new position
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()
