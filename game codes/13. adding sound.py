import pygame
import random
import sys

pygame.init()
#load the sound but does not play it
crash_sound = pygame.mixer.Sound("crash.wav")

#loads the music but doesnt play it
pygame.mixer.music.load("084_jazz_3.aif")
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
score = 0
player_size = 50
player_pos = [WIDTH / 2, HEIGHT - (2 * player_size)]
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
SPEED = 10
myFont = pygame.font.SysFont("monospace", 35)
clock = pygame.time.Clock()


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if ((e_y + enemy_size) >= 500):
        if ((e_x + enemy_size) < p_x or (e_x > p_x)):
            return False
        else:
            return True


screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = True

stop_sound = False

pygame.mixer.music.play(-1)
while game_over:
    #music_player()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x = x - player_size
            elif event.key == pygame.K_RIGHT:
                x = x + player_size
            player_pos = [x, y]

    screen.fill(BACKGROUND_COLOR)

    delay = random.random()
    print(delay)
    if (len(enemy_list) < 6 and delay < 0.02):
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        enemy_list.append(enemy_pos)

    for x in enemy_list:
        if x[1] >= 0 and x[1] < HEIGHT:
            x[1] += SPEED
        else:
            x[0] = random.randint(0, WIDTH - enemy_size)
            x[1] = 0
            score = score + 1
    print(score)
    text = "Score: " + str(score)
    label = myFont.render(text, 1, (255, 0, 0))
    screen.blit(label, (WIDTH - 200, HEIGHT - 40))

    for x in enemy_list:
        if detect_collision(player_pos, x):
            #game_over = False
            stop_sound = True

    if stop_sound:
        pygame.mixer.music.stop()
        crash_sound.play()
        #pygame.mixer.Sound.play(crash_sound)

    if stop_sound != True:
        for x in enemy_list:
            pygame.draw.rect(screen, BLUE, (x[0], x[1], enemy_size, enemy_size))
        pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
        clock.tick(30)
        pygame.display.update()

play_game()