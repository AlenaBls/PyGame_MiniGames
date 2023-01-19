import pygame as pg
from helper_def import *
from level import *


class Race:
    def __init__(self):
        pg.init()

        pg.display.set_caption('Race')
        self.screen = pg.display.set_mode((800, 600))
        self.buttons = pg.sprite.Group()
        self.fps = 30
        self.num = 1
        clock = pg.time.Clock()

        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.render(self.buttons)
            self.update_back()
            self.num = (self.num + 1) % 16
            clock.tick(self.fps)
            pg.display.flip()

        pg.quit()

    def render(self, group):
        self.screen.fill(pg.Color('#474a51'))
        name = pg.sprite.Sprite()
        name.image = load_img('race', 'race_name.png')
        name.rect = name.image.get_rect()
        name.rect.x, name.rect.y = [225, 0]
        group.add(name)
        interface(self, group)
        generate_level(load_level('level.txt'))

    def update_back(self):
        generate_back(load_back('decor.txt', self.num))


if __name__ == '__main__':
    Race()
    pg.quit()
