import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
BLUE = (0,0,255)
BACKGROUND_COLOR = (0,0,0)
player_size = 50
player_pos = [WIDTH/2,HEIGHT-(2*player_size)]

enemy_size = 50
#enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
# here, the x component of the enemy's position is randomised.
# 'random.randint' asks if we can create an enemy that starts from zero up to the width of the screen minus the enemy size
enemy_pos = [random.randint(0,WIDTH-enemy_size),random.randint(0,HEIGHT-enemy_size)] # to randomise both x and y


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
            # I added this for it to move up and down :) ;)
            elif event.key == pygame.K_UP:
                y = y - player_size
            elif event.key == pygame.K_DOWN:
                y = y + player_size

            player_pos = [x,y]
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()