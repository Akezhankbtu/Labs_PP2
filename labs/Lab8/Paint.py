import pygame
import math

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # Белый фон

clock = pygame.time.Clock()
colors = {
    pygame.K_1: (255, 0, 0),    # Красный
    pygame.K_2: (0, 255, 0),    # Зелёный
    pygame.K_3: (0, 0, 255),    # Синий
    pygame.K_4: (255, 255, 0),  # Жёлтый
    pygame.K_5: (0, 0, 0),      # Чёрный
}
current_color = colors[pygame.K_1]

# Начальные переменные
LMBpressed = False
THICKNESS = 5
figure_index = 0
tools = ['line', 'rect', 'circle', 'eraser']
tool = tools[figure_index]

# Координаты мыши
curr_x = 0
curr_y = 0
prev_x = 0
prev_y = 0
start_pos = (0, 0)

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_figure(tool_name, start, end, surface):
    if tool_name == 'line':
        pygame.draw.line(surface, current_color, start, end, THICKNESS)
    elif tool_name == 'rect':
        rect = calculate_rect(start[0], start[1], end[0], end[1])
        pygame.draw.rect(surface, current_color, rect, THICKNESS)
    elif tool_name == 'circle':
        center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        radius = int(math.hypot(end[0] - start[0], end[1] - start[1]) / 2)
        pygame.draw.circle(surface, current_color, center, radius, THICKNESS)
    elif tool_name == 'eraser':
        pygame.draw.circle(surface, (255, 255, 255), end, 15)

running = True
while running:
    screen.blit(base_layer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key in colors:
                current_color = colors[event.key]
            if event.key == pygame.K_UP:
                figure_index = (figure_index + 1) % len(tools)
                tool = tools[figure_index]
            if event.key == pygame.K_DOWN:
                figure_index = (figure_index - 1) % len(tools)
                tool = tools[figure_index]
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)

        # Нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            start_pos = event.pos
            prev_x, prev_y = event.pos

        # Отпуск мыши
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            end_pos = event.pos
            if tool in ['rect', 'circle']:
                draw_figure(tool, start_pos, end_pos, base_layer)

        # Движение мыши
        if event.type == pygame.MOUSEMOTION:
            curr_x, curr_y = event.pos
            if LMBpressed:
                if tool == 'line':
                    pygame.draw.line(base_layer, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
                    prev_x, prev_y = curr_x, curr_y
                elif tool == 'eraser':
                    draw_figure(tool, None, (curr_x, curr_y), base_layer)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()