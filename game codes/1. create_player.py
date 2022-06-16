import pygame
import sys

pygame.init()

WIDTH = 800 #width of the screen
HEIGHT = 600 #height of the screen
RED = (255,0,0)  #colour= (R, G, B)
player_pos = [400,300]
player_size = 50

screen = pygame.display.set_mode((WIDTH,HEIGHT)) #draws the screen using the preset with and height

not_game_over = True #preset for the while loop

while not_game_over: #while loop to keep the game running using the "not_game_over" preset
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks the event type
            pygame.quit() #end the game
            sys.exit() # shut down resources in the game
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()

# this is what the game screen looks like
# 0,0
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |