from pygame import *
from random import randint
from time import sleep

from Shooter.shooter_game import shooter_game, restart_shooter
from labirint.maze import labirint_game, restart_labirint
from Korsinka.korsinka import korsinka_game

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 144
GAME_FINISHED, GAME_RUN = False, True

CLOCK = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, position, size, speed=0):
        super().__init__()
        
        self.image = transform.scale(
            image.load(img),
            size
        )
        
        self.width, self.height = size
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        
        self.speed = speed
        
    def draw(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        pass
        
class Button(GameSprite):
    def __init__(self, img, position, size, func, speed=0):
        super().__init__(img, position, size, speed)
        
        self.func = func

# ! Функции кнопок
def func_btn1():
    global game, WINDOW
    
    mixer.music.load("Shooter//dream.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.2)
    
    restart_shooter()
    
    game = 2 
    WINDOW = display.set_mode((700, 500))

def func_btn2():
    
    global game, WINDOW
    
    mixer.music.load("labirint//jugles.mp3")
    mixer.music.play()
    
    restart_labirint()
    
    game = 3
    WINDOW = display.set_mode((500, 500))

def func_btn3():
    
    global game, WINDOW
    
    korsinka_game()
    
    game = 4
    WINDOW = display.set_mode((700, 500))
    
# ! Спрайты
btn1 = Button(img="btn.png", 
              position=(46, 200), 
              size=(104, 104), 
              func=func_btn1)

btn2 = Button(img="btn3.png", 
              position=(196, 200), 
              size=(104, 104), 
              func=func_btn2)

btn3 = Button(img="btn4.png", 
              position=(356, 200), 
              size=(104, 104), 
              func=func_btn3)



# ! Музыка
mixer.init()
mixer.music.load("bg.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.5)
# ?
# ?
# ?

# ! Текст
font.init()
stats_font = font.Font("code.ttf", 42)
controll_font = font.Font("code.ttf", 22)
name_text = stats_font.render("Mastergame", True, (20, 130, 200))
controll_text = controll_font.render("A D    W A S D    A D", True, (20, 130, 120))
# ?
# ?

game = 1

btns_group = sprite.Group()
btns_group.add(btn1, btn2, btn3)

# ?

# ! Игровой цикл
while GAME_RUN:
    
    for ev in event.get():
        if ev.type == QUIT:
            GAME_RUN = False
        if ev.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = ev.pos
            for btn in btns_group:
                if btn.rect.collidepoint(mouse_x, mouse_y) and game == 1:
                    btn.func()

    if not GAME_FINISHED:
        
        if game == 1:
            WINDOW.fill((0, 0, 0))
            WINDOW.blit(name_text, (70, 10))
            WINDOW.blit(controll_text, (56, 360))
            btns_group.draw(WINDOW)
            
        if game == 2:
            is_ended = shooter_game()
            
            if is_ended:
                sleep(2)
        
                mixer.music.load("bg.mp3")
                mixer.music.play(-1)
                
                game = 1
                WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            
        if game == 3:
            is_ended = labirint_game()
            
            if is_ended:
                sleep(2)
        
                mixer.music.load("bg.mp3")
                mixer.music.play(-1)
                
                game = 1
                WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            
        if game == 4:
            is_ended = korsinka_game()
            
            if is_ended:
        
                mixer.music.load("bg.mp3")
                mixer.music.play(-1)
                
                game = 1
                WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    display.update()
    CLOCK.tick(FPS)
