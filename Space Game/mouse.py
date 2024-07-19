import pygame

# INITIALIZE THE PYGAME
pygame.init()

# CREATE THE SCREEN
screen = pygame.display.set_mode((800, 600))

# TITLE AND ICON
pygame.display.set_caption("Starship Strike")
icon = pygame.image.load("ok.png")  # Ensure the file "ok.png" is in the same directory
pygame.display.set_icon(icon)

# PLAYER
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 500

def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means to draw

# GAME LOOP
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player position based on mouse position
    mouseX, _ = pygame.mouse.get_pos()
    playerX = mouseX - playerImg.get_width() / 2

    # Ensure the player stays within the screen bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - playerImg.get_width():
        playerX = 800 - playerImg.get_width()

    # Draw the player
    player(playerX, playerY)
    
    pygame.display.update()

pygame.quit()
