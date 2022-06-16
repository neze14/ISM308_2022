import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
BLACK = (0,0,0)
#BLUE = (0,0,255)
BACKGROUND_COLOR = (255,255,255)
# BACKGROUND_COLOR = (0,0,0)
player_size = 50
player_pos = [WIDTH/2,HEIGHT-(2*player_size)]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]


screen = pygame.display.set_mode((WIDTH,HEIGHT))

not_game_over = True

while  not_game_over:
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
            # I added this for it to move up and down :) ;)
            elif event.key == pygame.K_UP:
                y = y - player_size
            elif event.key == pygame.K_DOWN:
                y = y + player_size

            player_pos = [x,y]

    screen.fill(BACKGROUND_COLOR)
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT: # if the enemy is between the minimum and maximum height of the game window
        enemy_pos[1] += 10 # add 10 to the y position of the enemy
    else:
        enemy_pos[1] = 0 # this reset the y position of the enemy to zero
    pygame.draw.rect(screen, BLACK, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()
