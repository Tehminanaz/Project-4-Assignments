import math
import random
import pygame
from pygame import mixer

# Initialize the pygame library
pygame.init()

# Create the game window (width=800, height=600)
screen = pygame.display.set_mode((800, 600))

# Load and set the background image
background = pygame.image.load('background.png')

# Load and play background music in a loop
mixer.music.load("background.wav")
mixer.music.play(-1)

# Set window title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Load player image and set starting position
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0  # How much player moves left or right

# Enemy setup
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6  # Total enemies

# Create multiple enemies with random starting positions
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)     # Enemy speed in x direction
    enemyY_change.append(40)    # How much enemy drops down after hitting edge

# Bullet setup
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10  # Speed of bullet
bullet_state = "ready"  # "ready" means bullet is hidden, "fire" means it's moving

# Score setup
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

# Game Over text font
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Function to show score on screen
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to display "Game Over" text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Draw the player on screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# Draw the enemy on screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Fire the bullet (display it on screen)
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # Slightly adjusted position

# Check for collision between bullet and enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

# Main game loop
running = True
while running:
    # Fill screen with black first
    screen.fill((0, 0, 0))
    
    # Display the background image
    screen.blit(background, (0, 0))

    # Event handling (key presses, closing game, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if arrow keys or space are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5  # Move left
            if event.key == pygame.K_RIGHT:
                playerX_change = 5   # Move right
            if event.key == pygame.K_SPACE:
                # Fire bullet only if it's ready
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # Stop movement when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update player position
    playerX += playerX_change

    # Keep player inside screen boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Update enemies
    for i in range(num_of_enemies):

        # End game if enemy reaches near player
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move enemies off-screen
            game_over_text()
            break

        # Move enemy
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Check for collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1  # Increase score
            # Reset enemy to new random position
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)  # Draw enemy

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Draw player
    player(playerX, playerY)

    # Show score
    show_score(textX, testY)

    # Refresh game screen
    pygame.display.update()
