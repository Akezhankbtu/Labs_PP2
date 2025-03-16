import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

# Начальные координаты шара
x = WIDTH // 2
y = HEIGHT // 2

# Радиус шара
radius = 25

# Скорость перемещения
velocity = 20

# Переменная для главного цикла
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее состояние
    keys = pygame.key.get_pressed()

    # Движение вверх
    if keys[pygame.K_UP]:
        if y - velocity - radius >= 0:
            y -= velocity

    # Движение вниз
    if keys[pygame.K_DOWN]:
        if y + velocity + radius <= HEIGHT:
            y += velocity

    # Движение влево
    if keys[pygame.K_LEFT]:
        if x - velocity - radius >= 0:
            x -= velocity

    # Движение вправо
    if keys[pygame.K_RIGHT]:
        if x + velocity + radius <= WIDTH:
            x += velocity

    # Заливаем фон белым цветом
    screen.fill((255, 255, 255))

    # Рисуем красный шар
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    # Обновляем экран
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
sys.exit()
