import pygame
from pygame import mixer
import time

# initialize the pygame
pygame.init()
# add background music
mixer.music.load("background.mp3")
mixer.music.play(-1)
# set the clock
clock = pygame.time.Clock()
# create the screen
scr = pygame.display.set_mode((800, 500))
# set title of the game
pygame.display.set_caption("pong game")
# set parameters of player stick 1
stick1X = 5
stick1Y = 250
stick1Y_change = 0
# set parameters of player stick 2
stick2X = 790
stick2Y = 250
stick2Y_change = 0
# set parameters of the ball
ballX = 400
ballY = 250
ballX_change = 4
ballY_change = 4
rad = 5
# to count the score and to display the score of each player
score_count1 = 0
score_count2 = 0
score_font = pygame.font.Font("freesansbold.ttf", 17)
score1 = 0
score2 = 0


# fuction to display scores
def score_board1():
    score = score_font.render("Player 1: " + str(score1), True, (255, 255, 255))
    scr.blit(score, (250, 5))


def score_board2():
    score = score_font.render("Player 2: " + str(score2), True, (255, 255, 255))
    scr.blit(score, (464, 5))


# to display the player 1
def stick1(x, y):
    pygame.draw.rect(scr, (255, 255, 255), (x, y, 4, 80))


# to display the player 2
def stick2(p, q):
    pygame.draw.rect(scr, (255, 255, 255), (p, q, 4, 80))


# to display the ball
def ball(x, y, z):
    pygame.draw.circle(scr, (255, 255, 255), (x, y), z)


# game loop
running = True
while running:
    pygame.time.delay(0)
    # to fill the screen after movement of players and ball
    scr.fill((0, 0, 0))
    # loop for player movement
    for events in pygame.event.get():
        # quit condition
        if events.type == pygame.QUIT:
            running = False
        # set keys for movement of players
        if events.type == pygame.KEYDOWN:
            # to move up for player at right
            if events.key == pygame.K_UP:
                stick2Y_change = -10
            # to move down for player at right
            if events.key == pygame.K_DOWN:
                stick2Y_change = 10
            # to move up for player at left
            if events.key == pygame.K_w:
                stick1Y_change = -10
            # to move down for player at left
            if events.key == pygame.K_s:
                stick1Y_change = 10
        # to stop the player stick after releasing the key
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP or events.key == pygame.K_DOWN or events.key == pygame.K_w or events.key == pygame.K_s:
                stick1Y_change = 0
                stick2Y_change = 0
    # movement of players
    stick1Y += stick1Y_change
    stick2Y += stick2Y_change

    # movement of ball
    ballX += ballX_change
    ballY += ballY_change
    # setting boundaries for ball and to make ball bounce
    if ballY >= 490:
        ballY_change *= -1
    if ballY <= 5:
        ballY_change *= -1
    # to make ball bounce on sticks of players
    if ballY in range(stick1Y - 4, stick1Y + 84) and (ballX) <= 13 and ballX >= 10:
        ballX_change *= -1
        bouncing_sound1 = mixer.Sound("bounce.wav")
        bouncing_sound1.play()
    if ballY in range(stick2Y - 4, stick2Y + 84) and (ballX) >= 785 and ballX <= 788:
        ballX_change *= -1
        bouncing_sound2 = mixer.Sound("bounce.wav")
        bouncing_sound2.play()
    # code to increase the score count when player misses the ball
    if ballX <= 5:
        score_count2 = 1
        lose1 = mixer.Sound("loose.wav")
        lose1.play()
        time.sleep(1)
        ballX = 400
        ballY = 250
        score2 += score_count2
    if ballX >= 795:
        score_count1 = 1
        lose2 = mixer.Sound("loose.wav")
        lose2.play()
        time.sleep(1)
        ballX = 400
        ballY = 250
        score1 += score_count1

    # set boundaries for players
    if stick1Y < 5:
        stick1Y = 5
    elif stick1Y > 415:
        stick1Y = 415

    if stick2Y < 5:
        stick2Y = 5
    elif stick2Y > 415:
        stick2Y = 415
    # recall all functions to display all components on screen
    ball(ballX, ballY, rad)
    stick1(stick1X, stick1Y)
    pygame.draw.rect(scr, (50, 50, 50), (400, 0, 1, 500))
    stick2(stick2X, stick2Y)
    score_board1()
    score_board2()
    # set frames per second
    clock.tick(60)
    pygame.display.update()
pygame.quit()
