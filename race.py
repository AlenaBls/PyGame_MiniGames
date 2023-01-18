import pygame as pg
from helper_def import *
from level import *


class Race:
    def __init__(self):
        pg.init()

        pg.display.set_caption('Race')
        self.screen = pg.display.set_mode((800, 600))
        self.buttons = pg.sprite.Group()
        clock = pg.time.Clock()

        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.render(self.buttons)
            pg.display.flip()

    def render(self, group):
        self.screen.fill(pg.Color('#474a51'))
        name = pg.sprite.Sprite()
        name.image = load_img('race', 'race_name.png')
        name.rect = name.image.get_rect()
        name.rect.x, name.rect.y = [225, 0]
        group.add(name)
        interface(self, group)
        generate_level(self, load_level('level.txt'))


if __name__ == '__main__':
    Race()
    pg.quit()
