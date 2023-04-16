from pygame import *

BLUE = (200, 255, 255)

width = 900
height = 700
win = display.set_mode((width, height))
display.set_caption("Пинг-Понг")
win.fill(BLUE)

clock = time.Clock()
FPS = 40

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y    
   
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < height - 100:
            self.rect.y += self.speed 
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
    def update_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_S] and self.rect.y < height - 100:
            self.rect.y += self.speed 
        if key_pressed[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def update(self):
        pass

ball = Ball("ball.png", width/2, height/2, 50, 50, 5)
player_right = Player("platforma.png", 875, 300, 20, 100, 5)
player_left = Player("platforma.png", 5, 300, 20, 100, 5)

game = True
while game:
    win.fill(BLUE)
    ball.reset()
    player_right.reset()
    player_left.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    #ball.update()
    #player_right.update_right()
    #player_left.update_left()

    display.update()
    clock.tick(FPS)