import pygame
import sys
import datetime

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Загрузка изображений
clock_face = pygame.image.load("clock.png")     
hand_minute = pygame.image.load("min_hand.png")   
hand_second = pygame.image.load("sec_hand.png")   

# Координаты центра
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    print(minutes)
    print(seconds)
    print("----")
    # Рассчитываем углы поворота 
    minute_angle = -(minutes * 6)-49     
    second_angle = -(seconds * 6)+60    

    # Поворот изображений
    rotated_minute = pygame.transform.rotate(hand_minute, minute_angle)
    rotated_second = pygame.transform.rotate(hand_second, second_angle)
    face_rect = clock_face.get_rect(center=(center_x, center_y))
    minute_rect = rotated_minute.get_rect(center=(center_x, center_y))
    second_rect = rotated_second.get_rect(center=(center_x, center_y))

    # Рисуем
    screen.fill((255, 255, 255))      
    screen.blit(clock_face, face_rect)    
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    # Обновляем экран
    pygame.display.flip()
    # FPS
    clock.tick(30)

pygame.quit()
sys.exit()
