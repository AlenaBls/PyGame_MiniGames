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
    return image


def load_level(filename):
    filename = "data/race/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [str(line) for line in mapFile.readline().split()]

    return list(level_map for i in range(8))


def interface(self, group):
    self.screen = pg.display.get_surface()
    for i in range(8):
        button = pg.sprite.Sprite()
        button.image = load_img('backgrounds', constants.BUTTONS[i])
        button.rect = button.image.get_rect()
        button.rect.x = constants.X[i]
        button.rect.y = constants.Y[i]
        self.buttons.add(button)
    group.draw(self.screen)


race_tile_images = {
    'asf': load_img('race/tiles', 'asf.png'),
    'asf_l': load_img('race/tiles', 'asf_l.png'),
    'asf_r': load_img('race/tiles', 'asf_r.png'),
    'grass_l': load_img('race/tiles', 'grass_l.png'),
    'grass_r': load_img('race/tiles', 'grass_r.png'),
    'plit_l': load_img('race/tiles', 'plit_l.png'),
    'plit_r': load_img('race/tiles', 'plit_r.png')
}

