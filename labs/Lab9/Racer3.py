import pygame
import random
import time

pygame.init()
W=400
H=600
sc=pygame.display.set_mode((W,H))
pygame.display.set_caption("Racer")

image_bg=pygame.image.load('Street.png')
image_player=pygame.image.load('Player.png')
image_enemy=pygame.image.load('Enemy.png')
image_coin_raw=pygame.image.load('Coin.png')

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
sound_coin=pygame.mixer.Sound('coin.mp3')

sound_crash=pygame.mixer.Sound('crash.wav')

font=pygame.font.SysFont("Verdana",60)
image_go=font.render("GAME OVER",True,(0,0,0))
image_go_rect=image_go.get_rect(center=(W//2,H//2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=image_player
        self.rect=self.image.get_rect()
        self.rect.centerx=W//2
        self.rect.bottom=H
        #  We can also do -> self.rect.midbottom = (WIDTH // 2, HEIGHT)
        self.speed=5
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed,0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed,0)
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>W:
            self.rect.right=W
    
class Enemy(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image=image_enemy
        self.rect=self.image.get_rect()
        self.speed=10
    def generate_rr(self):
        self.rect.left=random.randint(0,W-self.rect.w)
        self.rect.bottom=0
    def move(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.top>H:
            self.generate_rr()
class Coin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.set_random_size_and_weight()# Set size and weigght
        self.rect=self.image.get_rect()
        self.generate_pos()
    def set_random_size_and_weight(self):
        size=random.choice([30,40,50])
        self.image=pygame.transform.scale(image_coin_raw,(size,size))
        self.weight=size//10
    def generate_pos(self):
        max_left=max(0,W-self.rect.width)
        self.rect.left=random.randint(0,max_left)
        self.rect.bottom=random.randint(-300,-50)
    def move(self):
        self.rect.move_ip(0,5)
        if self.rect.top>H:
            self.set_random_size_and_weight()
            self.rect=self.image.get_rect()
            self.generate_pos()

clock=pygame.time.Clock()
fps=60
player=Player()
enemy=Enemy()
coin=Coin()
coin_sprites=pygame.sprite.Group()
coin_sprites.add(coin)
all_sprites=pygame.sprite.Group()
enemy_sprites=pygame.sprite.Group()

all_sprites.add(player,enemy,coin)
enemy_sprites.add(enemy)
running=True
score=0
enemy_speed_increase_step=5
score_font=pygame.font.SysFont("Verdana",20)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    player.move()
    sc.blit(image_bg,(0,0))

    for entity in all_sprites:
        entity.move()
        sc.blit(entity.image,entity.rect)
    if pygame.sprite.spritecollideany(player,coin_sprites):
        score+=coin.weight
        sound_coin.play()
        coin.kill()# Удаляем старую монету и создаём новую
        coin=Coin()
        coin_sprites.add(coin)
        all_sprites.add(coin)

        if score%enemy_speed_increase_step==0:# Увеличиваем скорость врага
            enemy.speed+=1

    if pygame.sprite.spritecollideany(player,enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running=False
        sc.fill((255,0,0))
        sc.blit(image_go,image_go_rect)
        pygame.display.update()
        time.sleep(3)
    #Scores text:
    score_text=score_font.render("Score:"+str(score),True,(0,0,0))
    sc.blit(score_text,(10,10))

    pygame.display.update()
    clock.tick(fps)