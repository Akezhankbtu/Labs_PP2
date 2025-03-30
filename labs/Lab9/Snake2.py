import pygame
import sys
import random

pygame.init()

# --- Настройки ---
W = 600
H = 600
Cell = 30
Grid_w = W // Cell
Grid_h = H // Cell

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Жылан")

# --- Цвета ---
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
GRAY   = (128, 128, 128)
GREEN  = (0, 255, 0)
RED    = (255, 0, 0)
YELLOW = (255, 255, 0)

# --- Сетка ---
def draw_grid():
    for i in range(Grid_h):
        for j in range(Grid_w):
            rect = pygame.Rect(j * Cell, i * Cell, Cell, Cell)
            pygame.draw.rect(sc, GRAY, rect, 1)

# --- Точка ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- Змейка ---
class Snake:
    def __init__(self):
        self.body = [Point(10, 10), Point(9, 10), Point(8, 10)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x >= Grid_w:
            self.body[0].x = 0
        if self.body[0].x < 0:
            self.body[0].x = Grid_w - 1
        if self.body[0].y >= Grid_h:
            self.body[0].y = 0
        if self.body[0].y < 0:
            self.body[0].y = Grid_h - 1

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(sc, RED, (head.x * Cell, head.y * Cell, Cell, Cell))
        for segment in self.body[1:]:
            pygame.draw.rect(sc, YELLOW, (segment.x * Cell, segment.y * Cell, Cell, Cell))

    def check_collision_wf(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            tail = self.body[-1]
            self.body.append(Point(tail.x, tail.y))
            return True
        return False

    def check_self_c(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

# --- Еда ---
class Food:
    def __init__(self):
        self.generate_random_food([])

    def generate_random_food(self, snake_body):
        while True:
            x = random.randint(0, Grid_w - 1)
            y = random.randint(0, Grid_h - 1)
            collision = False
            for segment in snake_body:
                if segment.x == x and segment.y == y:
                    collision = True
                    break
            if not collision:
                self.pos = Point(x, y)
                self.weight = random.choice([1, 2, 3])
                self.time_created = pygame.time.get_ticks()
                break

    def draw(self):
        if self.weight == 1:
            color = GREEN
        elif self.weight == 2:
            color = (0, 150, 255)
        else:
            color = (255, 0, 255)
        pygame.draw.rect(sc, color, (self.pos.x * Cell, self.pos.y * Cell, Cell, Cell))
clock = pygame.time.Clock()
FPS = 5
snake = Snake()
food = Food()
score = 0
font = pygame.font.SysFont("Verdana", 25)
running = True

#Игровой цикл
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0

    snake.move()

    # Если съел еду
    if snake.check_collision_wf(food):
        score += food.weight
        food.generate_random_food(snake.body)

    # Если прошло больше 5 секунд — заменить еду
    current_time = pygame.time.get_ticks()
    if current_time - food.time_created > 5000:
        food.generate_random_food(snake.body)

    # Если врезался в себя
    if snake.check_self_c():
        running = False

    # Отрисовка
    sc.fill(BLACK)
    draw_grid()
    snake.draw()
    food.draw()
    score_text = font.render("Score: " + str(score), True, WHITE)
    sc.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
sys.exit()