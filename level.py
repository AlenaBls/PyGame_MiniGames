from helper_def import *
from constants import *

all_sprites = pg.sprite.Group()
tiles_group = pg.sprite.Group()


def generate_level(self, mape):
    self.screen = pg.display.get_surface()
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
        all_sprites.draw(self.screen)


class Tile(pg.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = race_tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            race_tile_width * pos_x + 150, race_tile_height * pos_y + 100)
