import pygame
import random
import math

# INITIALIZE PYGAME
pygame.init()

# SCREEN SETTINGS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)

# BACKGROUND SETTINGS
BACKGROUND_IMAGE = pygame.image.load("space3.jpg")
background = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND_X, BACKGROUND_Y = 0, 0

# TITLE AND ICON SETTINGS
pygame.display.set_caption("Starship Strike")
ICON_IMAGE = pygame.image.load("ok.png")
pygame.display.set_icon(ICON_IMAGE)

# PLAYER SETTINGS
PLAYER_IMAGE = pygame.image.load("player.png")
PLAYER_START_X, PLAYER_START_Y = 370, 500
player_x, player_y = PLAYER_START_X, PLAYER_START_Y
player_x_change = 0

# ENEMY SETTINGS
ENEMY_IMAGE = pygame.image.load("enemy.png")
NUMBER_OF_ENEMIES = 6
enemies = []
for _ in range(NUMBER_OF_ENEMIES):
    enemies.append({
        'image': ENEMY_IMAGE,
        'x': random.randint(0, 736),
        'y': random.randint(50, 150),
        'x_change': 0.3,
        'y_change': 80
    })

# BULLET SETTINGS
BULLET_IMAGE = pygame.image.load("bullet.png")
BULLET_Y_CHANGE = 0.2
bullets = []

# SCORE SETTINGS
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
SCORE_X, SCORE_Y = 10, 10

# GAME OVER SETTINGS
over_font = pygame.font.Font('freesansbold.ttf', 64)

def draw_player(x, y):
    screen.blit(PLAYER_IMAGE, (x, y))

def draw_enemy(enemy):
    screen.blit(enemy['image'], (enemy['x'], enemy['y']))

def fire_bullet(x, y):
    bullets.append([x + 16, y + 10])

def is_collision(obj_x, obj_y, bullet_x, bullet_y):
    distance = math.sqrt((obj_x - bullet_x)**2 + (obj_y - bullet_y)**2)
    return distance < 27

def show_score(x, y):
    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# MAIN GAME LOOP
running = True
game_over = False
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (BACKGROUND_X, BACKGROUND_Y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2
            if event.key == pygame.K_SPACE:
                fire_bullet(player_x, player_y)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    if not game_over:
        # Update player position
        player_x += player_x_change
        player_x = max(0, min(player_x, SCREEN_WIDTH - 64))

        # ENEMY MOVEMENT
        for enemy in enemies:
            enemy['x'] += enemy['x_change']
            if enemy['x'] <= 0:
                enemy['x_change'] = 0.2
                enemy['y'] += enemy['y_change']
            elif enemy['x'] >= SCREEN_WIDTH - 64:
                enemy['x_change'] = -0.2
                enemy['y'] += enemy['y_change']

            # Check for collision with player
            if is_collision(player_x, player_y, enemy['x'], enemy['y']):
                game_over = True

            # BULLET MOVEMENT AND COLLISION
            for bullet in bullets:
                screen.blit(BULLET_IMAGE, (bullet[0], bullet[1]))
                bullet[1] -= BULLET_Y_CHANGE
                if bullet[1] <= 0:
                    bullets.remove(bullet)
                if is_collision(enemy['x'], enemy['y'], bullet[0], bullet[1]):
                    bullets.remove(bullet)
                    score += 1
                    enemy['x'] = random.randint(0, 736)
                    enemy['y'] = random.randint(50, 150)

            draw_enemy(enemy)

        # Draw the player
        draw_player(player_x, player_y)

        # Show score
        show_score(SCORE_X, SCORE_Y)

    else:
        game_over_text()

    pygame.display.update()

pygame.quit()
