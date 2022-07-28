from time import time as timer
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.y < win_width-65:
            self.rect.x += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y > 100:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update

back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
