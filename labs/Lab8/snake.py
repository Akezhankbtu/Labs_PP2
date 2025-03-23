import pygame
import random
import sys

from color_palette import *  # Мысалы, мұнда colorWHITE, colorGRAY, colorYELLOW, colorRED, colorGREEN анықталған

pygame.init()

# Терезенің өлшемдері және тор өлшемі
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

CELL = 30  # Әр ұяшықтың өлшемі (пиксель)
GRID_WIDTH = WIDTH // CELL  # Тордың көлденең ұяшық саны
GRID_HEIGHT = HEIGHT // CELL  # Тордың тігінен ұяшық саны

# Ойын параметрлері
initial_FPS = 5  # Бастапқы FPS
FPS = initial_FPS
clock = pygame.time.Clock()

# Шрифттер (есеп пен деңгейді шығару үшін)
font = pygame.font.SysFont("Verdana", 24)

# Шахмат тақтасы тәрізді торды салу функциясы
def draw_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            pygame.draw.rect(screen, colors[(i+j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x  # x координатасы
        self.y = y  # y координатасы

    def __str__(self):
        return f"{self.x}, {self.y}"

# Функция: тамақтың кездейсоқ орнын генерациялау
def generate_food_position(snake):
    while True:
        # Қабырға ұяшықтарын өткізіп, ішкі ұяшықтардан кездейсоқ таңдау (1 мен GRID_WIDTH-2 аралығында)
        x = random.randint(1, GRID_WIDTH - 2)
        y = random.randint(1, GRID_HEIGHT - 2)
        collision = False
        for segment in snake.body:
            if segment.x == x and segment.y == y:
                collision = True
                break
        if not collision:
            return Point(x, y)

# Змейка класы
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Бастапқы дене сегменттері
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # Горизонталь жылжу бағыты
        self.dy = 0  # Вертикаль жылжу бағыты

    def move(self):
        # Дененің әр сегменті өзінен алдыңғысының орнына көшу
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        # Жетекші сегментті жылжыту
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_food_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            return True
        return False

    def grow(self):
        # Соңғы сегменттің орнына жаңа сегмент қосу
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

    def check_wall_collision(self):
        head = self.body[0]
        # Егер голова тордан тыс шықса – қабырғаға соқтығысты
        if head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= GRID_HEIGHT:
            return True
        return False

# Тамақ класы
class Food:
    def __init__(self, snake):
        self.pos = generate_food_position(snake)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def reposition(self, snake):
        self.pos = generate_food_position(snake)

# Ойынның бастапқы жағдайы: змейка, тамақ, есеп және деңгей
snake = Snake()
food = Food(snake)
score = 0
level = 1

running = True
while running:
    # Оқиғаларды өңдеу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Қате бағытқа өтуге жол бермеу үшін қарсы бағытқа тікелей бұрылуды тоқтатады
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    snake.move()

    # Қабырға соқтығысын тексеру
    if snake.check_wall_collision():
        running = False  # Егер соқтығысу болса, ойын аяқталады

    # Тамақпен соқтығысу тексерісі
    if snake.check_food_collision(food):
        snake.grow()         # Змейканы ұзартады
        score += 1           # Есепті арттырады
        food.reposition(snake)  # Тамақты жаңа орынға қояды

        # Әр 3 тамақ жинағанда деңгей артатыны және FPS өсетіні
        if score % 3 == 0:
            level += 1
            FPS += 1

    
    draw_chess()
    snake.draw()
    food.draw()

    
    info_text = font.render(f"Score: {score}  Level: {level}", True, (0, 0, 0))
    screen.blit(info_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
