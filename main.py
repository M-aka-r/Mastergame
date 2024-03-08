from pygame import *
from random import randint

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
    print("КНОПКА 1 НАЖАТА")

def func_btn2():
    print("КНОПКА 2 НАЖАТА")

def func_btn3():
    print("КНОПКА 3 НАЖАТА")

def func_btn4():
    import Korsinka.korsinka
    
    
# ! Спрайты
btn1 = Button(img="btn.png", 
              position=(96, 100), 
              size=(104, 104), 
              func=func_btn1)

btn2 = Button(img="btn2.png", 
              position=(300, 100), 
              size=(104, 104), 
              func=func_btn2)

btn3 = Button(img="btn3.png", 
              position=(300, 296), 
              size=(104, 104), 
              func=func_btn3)

btn4 = Button(img="btn4.png", 
              position=(96, 296), 
              size=(104, 104), 
              func=func_btn4)



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
name_text = stats_font.render("Mastergame", True, (20, 130, 200))
# ?
# ?

game = 1

btns_group = sprite.Group()
btns_group.add(btn1, btn2, btn3, btn4)

# ?

# ! Игровой цикл
while GAME_RUN:
    
    for ev in event.get():
        if ev.type == QUIT:
            GAME_RUN = False
        if ev.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = ev.pos
            for btn in btns_group:
                if btn.rect.collidepoint(mouse_x, mouse_y):
                    GAME_RUN = False
                    btn.func()

    if not GAME_FINISHED:
        if game == 1:
            WINDOW.blit(name_text, (70, 10))
            btns_group.draw(WINDOW)
    
    display.update()
    CLOCK.tick(FPS)