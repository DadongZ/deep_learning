import pygame
import random
import sys

pygame.init()

WIDTH=800
HEIGHT=800
RED= (255, 0, 0)
BLUE= (0, 0, 255)
BACKGROUND= (0, 0, 0)

player_size =50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()
SPEED = 10

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]
    screen.fill(BACKGROUND)
    # Update enemy pos
    if enemy_pos[1] >=0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += SPEED
    else:
        enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
        enemy_pos[1] = 0

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
        
    clock.tick(30)
    
    pygame.display.update()