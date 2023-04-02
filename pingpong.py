import pygame
import random

# Инициализация Pygame
pygame.init()

# Определим цвета
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

# Определим константы для размера окна и скорости
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED = 1
PADDLE_SPEED = 2

# Создание окна и установка заголовка
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong')

# Создание ракеток
paddle_left = pygame.Rect(50, 250, 20, 100)
paddle_right = pygame.Rect(730, 250, 20, 100)

# Создание мяча
ball = pygame.Rect(395, 295, 10, 10)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Функция для отображения объектов
def draw_objects():
    # Отрисовка ракеток и мяча
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.rect(screen, WHITE, ball)

# Функция для движения мяча
def move_ball():
    global ball_speed_x, ball_speed_y
    # Изменение положения мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Отскок мяча от верхней и нижней стенок
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    # Проверка, достиг ли мяч левой или правой стенки
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    # Проверка, достиг ли мяч ракетки
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed_x *= -1

# Функция для движения ракеток
def move_paddles():
    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    # Движение левой ракетки
    if keys[pygame.K_w] and paddle_left.top > 0:
        paddle_left.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_left.bottom < SCREEN_HEIGHT:
        paddle_left.y += PADDLE_SPEED
    # Движение правой ракетки
    if keys[pygame.K_UP] and paddle_right.top > 0:
        paddle_right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_right.bottom < SCREEN_HEIGHT:
        paddle_right.y += PADDLE_SPEED

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(BLACK)

    # Отображение объектов
    draw_objects()

    # Движение мяча и ракеток
    move_ball()
    move_paddles()

    # Обновление экрана
    pygame.display.flip()
