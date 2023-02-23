import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surf = test_font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    return []

def collisions(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.colliderect(obstacle_rect):
                return False
    return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()
start_time = 0
score = 0
game_active = False

# Sky
sky_surf = pygame.image.load('graphics/Sky.png').convert_alpha()

# Ground
ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()

# Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_list = []

# Player
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title = test_font.render('Pixel Runner', False, (111, 196, 169))
game_title_rect = game_title.get_rect(center = (400, 80))

start_instructions = test_font.render('Press Space to start the game!', False, (111, 196, 169))
start_instructions_rect = start_instructions.get_rect(center = (400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)


# game loop
while True:

    # even loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                        player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else :
                    obstacle_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 100)


    if game_active:
        # sky
        screen.blit(sky_surf, (0, 0))

        # Ground
        screen.blit(ground_surf, (0, 300))

        # Score
        score = display_score()

        # Obstacles
        obstacle_list = obstacle_movement(obstacle_list)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        game_active = collisions(obstacle_list)

    else:
        screen.fill((94, 129, 162))

        title_score = test_font.render(f'Score: {score}', False, (111, 196, 169))
        title_score_rect = title_score.get_rect(center = (400, 320))

        obstacle_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0 

        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title, game_title_rect)

        if score == 0: screen.blit(start_instructions, start_instructions_rect)
        else: screen.blit(title_score, title_score_rect)

    pygame.display.update()
    clock.tick(60)
