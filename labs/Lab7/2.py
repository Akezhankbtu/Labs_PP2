import pygame
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

playlist = [
    "Almaty-Semey.mp3",
    "Fairy.mp3",
    "Mockinbird.mp3"
]

current_index = 0

def play_song(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

# Сразу играем первый трек
play_song(current_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # Пауза (P)
            if event.key == pygame.K_p:
                pygame.mixer.music.pause()

            # Возобновить (W)
            elif event.key == pygame.K_w:
                pygame.mixer.music.unpause()

            # Остановить (S)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

            # Следующий (D)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                current_index = (current_index + 1) % len(playlist)
                play_song(current_index)

            # Предыдущий (A)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                current_index = (current_index - 1) % len(playlist)
                play_song(current_index)

            # Выход (Q)
            elif event.key == pygame.K_q:
                running = False

    screen.fill((50, 50, 50))
    pygame.display.flip()

pygame.quit()
sys.exit()
