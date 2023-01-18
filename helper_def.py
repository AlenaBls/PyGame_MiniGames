import os
import sys
import constants
import pygame as pg
pg.init()


def load_img(path, name, colorkey=None):
    fullname = os.path.join('data', path, name)
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level():
    pass


def interface(self):
    self.screen = pg.display.get_surface()
    self.buttons = pg.sprite.Group()
    for i in range(8):
        button = pg.sprite.Sprite()
        button.image = load_img('backgrounds', constants.BUTTONS[i])
        button.rect = button.image.get_rect()
        button.rect.x = constants.X[i]
        button.rect.y = constants.Y[i]
        self.buttons.add(button)
    self.buttons.draw(self.screen)