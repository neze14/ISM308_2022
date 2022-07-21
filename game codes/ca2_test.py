import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BACKGROUND_COLOR = (255,255,0)

player_size = 50
player_pos = [600,random.randint(0,HEIGHT-player_size)]
#player_pos = [600,random.randint(0,HEIGHT-player_size)]
#player_pos = [600,HEIGHT-(2*player_size)]

enemy_size = 50
enemy_pos = [0,0]
#enemy_pos = [random.randint(0,WIDTH-enemy_size),0]

SPEED = 10
clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_y + enemy_size) > 500:
        if (e_x + enemy_size) < p_x  or (e_x > p_x + player_size):
            return False
        else:
            return True

screen = pygame.display.set_mode((WIDTH,HEIGHT))

not_game_over = True

while  not_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_UP:
                y = y - player_size
            elif event.key == pygame.K_DOWN:
                y = y + player_size

            # for further potential mobility
            #elif event.key == pygame.K_LEFT:
                #x = x- player_size
            #elif event.key == pygame.K_RIGHT:
                #x = x + player_size

            player_pos = [x,y]

    screen.fill(BACKGROUND_COLOR)

    if enemy_pos[0] >= 0 and enemy_pos[0] < WIDTH:
        enemy_pos[0] += SPEED
    else:
        enemy_pos[0] = 0
        enemy_pos[1] = player_pos[1]

    if detect_collision(player_pos, enemy_pos):
        not_game_over = False

    if enemy_pos[0] < WIDTH/2:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    else:
        pygame.draw.rect(screen, GREEN, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    clock.tick(20)
    pygame.display.update()