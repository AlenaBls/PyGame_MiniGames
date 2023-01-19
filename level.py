from helper_def import race_tile_images
from constants import *
import pygame as pg

all_sprites = pg.sprite.Group()
tiles_group = pg.sprite.Group()
back_group = pg.sprite.Group()


def generate_level(mape):
    screen = pg.display.get_surface()
    x, y = None, None
    for y in range(len(mape)):
        for x in range(len(mape[y])):
            if mape[y][x] == '0':
                Tile('asf', x, y)
            elif mape[y][x] == '1':
                Tile('grass_l', x, y)
            elif mape[y][x] == '2':
                Tile('plit_l', x, y)
            elif mape[y][x] == '4':
                Tile('asf_l', x, y)
            elif mape[y][x] == '5':
                Tile('asf_r', x, y)
            elif mape[y][x] == '6':
                Tile('plit_r', x, y)
            elif mape[y][x] == '7':
                Tile('grass_r', x, y)
    tiles_group.draw(screen)


def generate_back(mape):
    x, y = None, None
    for y in range(len(mape)):
        for x in range(len(mape[y])):
            if mape[y][x] == '1':
                Back('btree_t', x, y - 1)
                Back('btree_b', x, y)
            elif mape[y][x] == '3':
                Back('lamp_t', x, y - 1)
                Back('lamp_b', x, y)
            elif mape[y][x] == '4':
                Back('bench_b1', x, y - 1)
                Back('bench_b2', x, y)
                Back('bench_b3', x, y - 2)
            elif mape[y][x] == '5':
                Back('trash', x, y)
            elif mape[y][x] == '7':
                Back('tree1', x, y)
            elif mape[y][x] == '8':
                Back('bench_s', x, y)
            elif mape[y][x] == '9':
                Back('flow', x, y)
            elif mape[y][x] == '3r':
                Back('lamp_tr', x, y - 1)
                Back('lamp_br', x, y)
            elif mape[y][x] == '8r':
                Back('bench_sr', x, y)
            elif mape[y][x] == '4r':
                Back('bench_b1r', x, y - 1)
                Back('bench_b2r', x, y)
                Back('bench_b3r', x, y - 2)


class Tile(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = race_tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            race_tile_width * pos_x + 150, race_tile_height * pos_y + 100)


class Back(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        screen = pg.display.get_surface()
        super().__init__(back_group)
        self.image = race_tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            race_tile_width * pos_x + 150, race_tile_height * pos_y + 100)
        back_group.draw(screen)
        self.kill()