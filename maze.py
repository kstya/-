from pygame import *
from GameSprite import GameSprite
from Player import Player
from Enemy import Enemy
from Wall import Wall
# создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")


# задай фон сцены
background = transform.scale(image.load("background.jpg"), (700, 500))
# Координаты спрайтов и начальные характеристики
x1, y1 = 100, 350
x2, y2 = 400, 350
x3, y3 = 625, 425
# Музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.play()
# Создание спрайтов
main_hero = Player("hero.png", x1, y1, 10, window)
enemy = Enemy('cyborg.png', x2, y2, 4, window)
money = GameSprite("treasure.png", x3, y3, 0, window)
# стена
wall = Wall(173, 255, 47, 20, 250, 350, 200, window)
wall1 = Wall(220, 20, 60, 20, 250, 200, 200, window)
wall2 = Wall(240, 230, 140, 20, 250, 380, 200, window)
FPS = 60
clock = time.Clock()
game = True
finish = False
while game:
    # Установка ФПС и обновление экрана
    clock.tick(FPS)

    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        main_hero.reset()

        main_hero.update()

        enemy.reset()

        enemy.update()

        money.reset()

        wall.draw_wall()
        wall1.draw_wall()
        wall2.draw_wall()

        if sprite.collide_rect(main_hero, money):
            finish = True
        if sprite.collide_rect(main_hero, enemy):
            finish = True
        if sprite.collide_rect(main_hero, wall) or sprite.collide_rect(main_hero, wall1) or sprite.collide_rect(main_hero, wall2):
            finish = True
        display.update()

