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
    
    Просмотр файла: c:\Users\Teacher\Desktop\Пинг Понг\button.py
import pygame


class Button:
    def __init__(
        self, x=0, y=0, width=10, height=10,
        text='Default', text_color=(240, 240, 240),
        normal_color=(92, 11, 143), hover_color=(179, 73, 245),
        font_size=20, font_family='Arial', center_x=True
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.font_family = font_family
        w_width, w_height = pygame.display.get_window_size()
        if center_x:
            window_rect = pygame.Rect(0, 0, w_width, w_height)
            self.rect.centerx = window_rect.centerx
        self.is_hovered = False
        self.font = pygame.font.SysFont(font_family, font_size)
    
    def draw(self, window):
        image = self.font.render(self.text, True, self.text_color)
        image_rect = image.get_rect()
        image_rect.center = self.rect.center
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.normal_color
        pygame.draw.rect(window, color, self.rect)
        window.blit(image, (image_rect.x, image_rect.y))

    def is_clicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.is_hovered = True
                    break
                else:
                    self.is_hovered = False

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((600, 400))
window.fill((253, 199, 255))
clock = pygame.time.Clock()

btn_start = Button(y=200, width=150, height=40, text='Начать игру')
btn_exit = Button(y=250, width=150, height=40, text='Выход')

game = True
while game:
    window.fill((253, 199, 255))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game = False
    
    btn_start.draw(window)
    btn_start.update(events)
    if btn_start.is_clicked(events):
        print('Игра начинается')

    btn_exit.draw(window)
    btn_exit.update(events)
    if btn_exit.is_clicked(events):
        print('Конец!')

    clock.tick(60)
    pygame.display.update()
