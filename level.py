from helper_def import race_tile_images
from helper_def import race_car_images
from helper_def import race_player_images
from constants import *
from random import randint
import pygame as pg

tiles_group = pg.sprite.Group()
back_group = pg.sprite.Group()
player_group = pg.sprite.Group()
cars_group = pg.sprite.Group()


def generate_level(mape):
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


def generate_back(mape):
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


def spawn_cars(score, num):
    if score % num == 0 and score != 0:
        Cars(CARS[randint(0, 2)], randint(250, 500), 50)
    cars_group.update()


def get_player(chosen_car):
    if chosen_car is None:
        player_image = PLAYERS[randint(0, 2)]
        player = Player(player_image, 375, 450)
        return player, player_image

    else:
        player_image = chosen_car[:-4]
        player = Player(player_image, 375, 450)
        return player, player_image


def move(direction, image, player):
    screen = pg.display.get_surface()
    player.image = image
    if direction == 'l':
        player.rect = player.image.get_rect().move(check(player.rect.x - 50), player.rect.y)
    if direction == 'r':
        player.rect = player.image.get_rect().move(check(player.rect.x + 50), player.rect.y)
    player_group.draw(screen)


def check(num):
    if num >= 575:
        return num - 50
    if num < 225:
        return num + 50
    else:
        return num


class Tile(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = race_tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            race_tile_width * pos_x + 150, race_tile_height * pos_y + 100)


class Back(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(back_group)
        self.image = race_tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            race_tile_width * pos_x + 150, race_tile_height * pos_y)

    def update(self, group):
        for tile in group:
            tile.rect = tile.image.get_rect().move(tile.rect.x, (tile.rect.y + 50) % 600)


class Player(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(player_group)
        self.image = race_player_images[tile_type]
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.mask = pg.mask.from_surface(self.image)


class Cars(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(cars_group)
        self.image = race_car_images[tile_type]
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def update(self):
        if self.rect.y + 50 < 500:
            self.rect = self.image.get_rect().move(self.rect.x, self.rect.y + 50)
        else:
            self.kill()

    def check(self, player):
        key = 1
        for car in self:
            if pg.sprite.collide_mask(car, player):
                key *= 0
        if key == 0:
            return True
