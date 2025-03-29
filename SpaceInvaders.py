# Space Invaders - pygame
import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("Assets/background.jpg")

# Background Sound

mixer.music.load("assets/background.wav")
mixer.music.play(-1)
print(mixer.music.get_volume())
mixer.music.set_volume(.10)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("assets/battleship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("assets/enemy1.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.15)
    enemyY_change.append(40)

# Bullet
# Ready (Can't see bullet) Fire (Bullet active)
bulletImg = pygame.image.load("assets/lasershot.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .5
bullet_state = "ready"


def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (225, 225, 225))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) +
                         math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB (MAX 255)
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        # Game Quit
        if event.type == pygame.QUIT:
            running = False
        # Keystroke pressed
        if event.type == pygame.KEYDOWN:
            print("Keystroke is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                print("Spacebar is pressed")
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('assets/laser.wav')
                    bullet_sound.play()
                    bullet_sound.get_volume()
                    bullet_sound.set_volume(.10)
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        #Keystroke - released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                playerX_change = 0

    # Player Movement Boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200, 250)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.15
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.15
            enemyY[i] += enemyY_change[i]
    # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('assets/explosion.wav')
            explosion_sound.play()
            explosion_sound.set_volume(.10)
            bulletY = 480
            bullet_state = "ready"
            score_value += 25
            print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        player(playerX, playerY)
        enemy(enemyX[i], enemyY[i], i)
        show_score(textX, textY)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    pygame.display.update()
