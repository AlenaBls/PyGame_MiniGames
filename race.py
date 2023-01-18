import pygame as pg
from helper_def import *


class Race:
    def __init__(self):
        pg.init()

        pg.display.set_caption('Race')
        self.screen = pg.display.set_mode((800, 600))
        clock = pg.time.Clock()
        fps = 20

        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.render()
            clock.tick(fps)
            pg.display.flip()

    def render(self):
        self.screen.fill(pg.Color('#474a51'))
        pg.draw.rect(self.screen, pg.Color('black'), (150, 100, 500, 400))
        interface(self)


if __name__ == '__main__':
    Race()
    pg.quit()
