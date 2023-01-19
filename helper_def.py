import os
import sys
import PIL
from PIL import Image
import constants
import pygame as pg


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


def load_back(filename, num):
    filename = "data/race/" + filename
    with open(filename, 'r') as mapFile:
        back_map = []
        for i in range(24):
            a = [str(line) for line in mapFile.readline().split()]
            if i in list(range(num, num + 8)):
                back_map.append(a)

    return back_map


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
    'plit_r': load_img('race/tiles', 'plit_r.png'),
    'bench_b1': load_img('race/tiles', 'bench_b1.png'),
    'bench_b2': load_img('race/tiles', 'bench_b2.png'),
    'bench_b3': load_img('race/tiles', 'bench_b3.png'),
    'bench_s': load_img('race/tiles', 'bench_s.png'),
    'btree_b': load_img('race/tiles', 'btree_b.png'),
    'btree_t': load_img('race/tiles', 'btree_t.png'),
    'flow': load_img('race/tiles', 'flow.png'),
    'lamp_b': load_img('race/tiles', 'lamp_b.png'),
    'lamp_t': load_img('race/tiles', 'lamp_t.png'),
    'trash': load_img('race/tiles', 'trash.png'),
    'tree1': load_img('race/tiles', 'tree1.png'),
    'bench_b1r': load_img('race/tiles', 'bench_b1r.png'),
    'bench_b2r': load_img('race/tiles', 'bench_b2r.png'),
    'bench_b3r': load_img('race/tiles', 'bench_b3r.png'),
    'bench_sr': load_img('race/tiles', 'bench_sr.png'),
    'lamp_br': load_img('race/tiles', 'lamp_br.png'),
    'lamp_tr': load_img('race/tiles', 'lamp_tr.png')
}

