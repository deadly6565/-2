import pygame
import random

pygame.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
 
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED = 1
PADDLE_SPEED = 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('пинг понг')

paddle_left = pygame.Rect(50, 250, 20, 100)
paddle_right = pygame.Rect(730, 250, 20, 100)

ball = pygame.Rect(395, 295, 10, 10)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

def draw_objects():
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.rect(screen, WHITE, ball)

def move_ball():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed_x *= -1



def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_left.top > 0:
        paddle_left.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_left.bottom < SCREEN_HEIGHT:
        paddle_left.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_right.top > 0:
        paddle_right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_right.bottom < SCREEN_HEIGHT:
        paddle_right.y += PADDLE_SPEED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    draw_objects()

    move_ball()
    move_paddles()

    pygame.display.flip()
