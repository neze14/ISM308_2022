import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
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
            if event.key == pygame.K_LEFT: #press left key(arrow) then do subtract 5 units from the position of the player
                x = x- 5
            elif event.key == pygame.K_RIGHT: #press right key(arrow) then do add 5 units to the position of the player
                x = x + 5
            player_pos = [x,y] # then reposition the player with new changes abd restart the while loop
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size)) #how ever the new box is redrawn over the old one making it appear to grow in size instead of moving
    pygame.display.update()