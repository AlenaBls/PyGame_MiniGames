import pygame as pg
from helper_def import *
from level import *


class Race:
    def __init__(self, chosen_car):
        pg.init()

        pg.display.set_caption('Race')
        self.screen = pg.display.set_mode((800, 600))
        self.buttons = pg.sprite.Group()
        self.player, image = get_player(chosen_car)
        image = load_img('race/cars', image + '.png')
        generate_level(load_level('level.txt'))
        generate_back(load_back('decor.txt'))
        self.render(self.buttons)
        self.num = 50
        self.fps = 5
        self.score = 0
        clock = pg.time.Clock()

        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        move('l', image, self.player)
                    if event.key == pg.K_d:
                        move('r', image, self.player)
            self.create_game()
            game_over = Cars.check(cars_group, self.player)
            pg.display.flip()
            self.score += 5
            self.fps += 0.1
            if game_over:
                self.start_again(self.score)
                for car in cars_group:
                    car.kill()
                self.score = 0
                self.fps = 5
            clock.tick(self.fps)

        pg.quit()

    def create_game(self):
        tiles_group.draw(self.screen)
        player_group.draw(self.screen)
        spawn_cars(self.score, self.num)
        cars_group.draw(self.screen)
        back_group.draw(self.screen)
        self.close()
        Back.update(self, back_group)
        pg.draw.rect(self.screen, (pg.Color('#474a51')), (0, 525, 800, 100))
        font = pg.font.Font(None, 40)
        text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (400 - (text.get_rect().width / 2), 525))

    def render(self, group):
        self.screen.fill(pg.Color('#474a51'))
        name = pg.sprite.Sprite()
        name.image = load_img('race', 'race_name.png')
        name.rect = name.image.get_rect()
        name.rect.x, name.rect.y = [225, 0]
        group.add(name)
        interface(self, group)

    def close(self):
        pg.draw.rect(self.screen, (pg.Color('#474a51')), (150, 0, 50, 100))
        pg.draw.rect(self.screen, (pg.Color('#474a51')), (150, 500, 50, 100))
        pg.draw.rect(self.screen, (pg.Color('#474a51')), (600, 0, 50, 100))
        pg.draw.rect(self.screen, (pg.Color('#474a51')), (600, 500, 50, 100))

    def start_again(self, score):
        self.screen.fill(pg.Color('#474a51'))
        font = pg.font.SysFont('georgia', 50)
        text = font.render('Game over!', True, (255, 255, 255))
        self.screen.blit(text, (400 - (text.get_rect().width / 2), 150 - (text.get_rect().height / 2)))
        text = font.render('Click to start again', True, (255, 255, 255))
        self.screen.blit(text, (400 - (text.get_rect().width / 2), 250 - (text.get_rect().height / 2)))
        text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (400 - (text.get_rect().width / 2), 325))
        pg.display.flip()
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.render(self.buttons)
                    waiting = False
