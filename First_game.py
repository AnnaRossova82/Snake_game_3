import pygame
import random
import time

speed_of_snake = 5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

white_color = pygame.Color(255, 255, 255)
black_color = pygame.Color(0, 0, 0)
red_color = pygame.Color(250, 0, 0)
green_color = pygame.Color(124, 252, 0)

pygame.init()

display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pygame.transform.scale(pygame.image.load('font.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

apple = pygame.transform.scale(pygame.image.load('apple.jpg'), (30, 30))
orange = pygame.transform.scale(pygame.image.load('orange.jpg'), (30, 30))
pear = pygame.transform.scale(pygame.image.load('pear.jpg'), (30, 30))
banana = pygame.transform.scale(pygame.image.load('banana.jpg'), (30, 30))

sb = pygame.transform.scale(pygame.image.load('snake_body_2.JPG'), (30, 30))

fruit_images = [apple, orange, pear, banana]

pygame.display.set_caption('PYTHON - SNAKE')

game_clock = pygame.time.Clock()

position_of_snake = [450, 500]

body_of_snake = [
    [450, 500],
    [440, 500],
    [430, 500],
    [420, 500]
]

position_of_fruit = [
    random.randrange(1, (SCREEN_WIDTH//10)) * 10,
    random.randrange(1, (SCREEN_HEIGHT//10)) * 10
]
spawning_of_fruit = True

position_of_fruit_2 = [
    random.randrange(1, (SCREEN_WIDTH//10)) * 10,
    random.randrange(1, (SCREEN_HEIGHT//10)) * 10
]
spawning_of_fruit_2 = True


initial_direction = 'UP'
snake_direction = initial_direction

player_score = 0

def display_score (selection, font_color, font_style, font_size):
    score_font_style = pygame.font.SysFont(font_style, font_size)
    score_surface = score_font_style.render('Your Score:' + str(player_score), True, font_color)
    score_rec = score_surface.get_rect()
    display_screen.blit(score_surface, score_rec)

def game_over():
    game_over_font_style = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font_style.render('Your score is:' + str(player_score), True, red_color)

    game_over_rec = game_over_surface.get_rect()
    game_over_rec.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    display_screen.blit(game_over_surface, game_over_rec)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


def game_win():
    game_win_font_style = pygame.font.SysFont('times new roman', 50)
    game_win_surface = game_win_font_style.render('Congratulations! Your Score is : 10', True, red_color)

    game_win_rec = game_win_surface.get_rect()
    game_win_rec.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    display_screen.blit(game_win_surface, game_win_rec)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

random_fruit_image = random.choice(fruit_images)

game_run = True

while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake_direction = 'DOWN'
            if event.key == pygame.K_UP:
                snake_direction = 'UP'
            if event.key == pygame.K_LEFT:
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake_direction = 'RIGHT'
            if event.key == pygame.K_w:
                snake_direction = 'UP'
            if event.key == pygame.K_a:
                snake_direction = 'LEFT'
            if event.key == pygame.K_s:
                snake_direction = 'DOWN'
            if event.key == pygame.K_d:
                snake_direction = 'RIGHT'

    if snake_direction == 'UP' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    if snake_direction == 'DOWN' and initial_direction != 'UP':
        initial_direction = 'DOWN'
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'

    if snake_direction == 'W' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    if snake_direction == 'S' and initial_direction != 'UP':
        initial_direction = 'DOWN'
    if snake_direction == 'A' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
    if snake_direction == 'D' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'

    
    display_screen.fill(white_color)
    display_screen.blit(bg, (0, 0))

    if initial_direction == 'UP':
        position_of_snake[1] -= 10
    if initial_direction == 'DOWN':
        position_of_snake[1] += 10
    if initial_direction == 'LEFT':
        position_of_snake[0] -= 10
    if initial_direction == 'RIGHT':
        position_of_snake[0] += 10
    
    body_of_snake.insert(0, list(position_of_snake))
    if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:
        player_score +=1
        spawning_of_fruit = False
    elif position_of_snake[0] == position_of_fruit_2[0] and position_of_snake[1] == position_of_fruit_2[1]:
        player_score +=1
        spawning_of_fruit_2 = False
    else:
        body_of_snake.pop()

    if not spawning_of_fruit:
        position_of_fruit = [
            random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT // 10)) * 10
        ]
    spawning_of_fruit = True
    
    if not spawning_of_fruit_2:
           position_of_fruit_2 = [
           random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
           random.randrange(1, (SCREEN_HEIGHT // 10)) * 10
       ]

    random_fruit_image = random.choice(fruit_images)

    spawning_of_fruit_2 = True
    
    for position in body_of_snake:
        # pygame.draw.rect(display_screen, black_color, pygame.Rect(position[0], position[1], 10, 10))
        display_screen.blit(sb, (position[0], position[1]))
        # pygame.draw.rect(display_screen, red_color, pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))
        display_screen.blit(random_fruit_image, (position_of_fruit[0], position_of_fruit[1]))
        display_screen.blit(random_fruit_image, (position_of_fruit_2[0], position_of_fruit_2[1]))

    if position_of_snake[0] < 0 or position_of_snake[0] > SCREEN_WIDTH - 10:
        game_over()
    if position_of_snake[1] < 0 or position_of_snake[1] > SCREEN_HEIGHT - 10:
        game_over()

    for block in body_of_snake[1:]:
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:
            game_over()

    display_score(1, pygame.Color(10, 25, 255), 'times new roman', 20)
    
    pygame.display.update()

    if player_score == 10:
        game_win()

    game_clock.tick(speed_of_snake)

pygame.quit()

