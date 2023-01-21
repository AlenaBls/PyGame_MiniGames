import pygame as pg
from helper_def import *
from level import *


class Race:
    def __init__(self):
        pg.init()

        pg.display.set_caption('Race')
        self.screen = pg.display.set_mode((800, 600))
        self.buttons = pg.sprite.Group()
        self.player, image = get_player()
        image = load_img('race/cars', image + '.png')
        generate_level(load_level('level.txt'))
        generate_back(load_back('decor.txt'))
        self.num = 20
        self.fps = 10
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
            if game_over:
                start_again(self.screen)
                game_over = False
                for car in cars_group:
                    car.kill()
                self.score = 0
            clock.tick(self.fps)

        pg.quit()

    def create_game(self):
        self.render(self.buttons)
        tiles_group.draw(self.screen)
        player_group.draw(self.screen)
        spawn_cars(self.score, self.num)
        cars_group.draw(self.screen)
        back_group.draw(self.screen)
        self.close()
        Back.update(self, back_group)
        font = pg.font.Font(None, 40)
        text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (320, 525))

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


if __name__ == '__main__':
    Race()
    pg.quit()
