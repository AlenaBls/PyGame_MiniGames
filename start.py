import pygame as pg
from race import Race
from helper_def import load_img
import constants


class Start:
    def __init__(self):
        pg.init()

        pg.display.set_caption('Race')
        self.screen = pg.display.set_mode((800, 600))
        self.interface()
        self.chosen_car = None

        self.starting = True
        while self.starting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.click(x, y)
                if event.type == pg.MOUSEMOTION:
                    x, y = event.pos
                    self.glow(x, y)
            pg.display.flip()
        pg.quit()

    def interface(self):
        self.screen.fill(pg.Color('#474a51'))

        starts = pg.sprite.Group()
        name = pg.sprite.Sprite()
        name.image = load_img('race', 'race_name.png')
        name.rect = name.image.get_rect()
        name.rect.x, name.rect.y = [225, 0]
        starts.add(name)

        font = pg.font.Font(None, 50)
        text = font.render('Choose your fighter', True, (255, 255, 255))
        self.screen.blit(text, (400 - (text.get_rect().width / 2), 150 - (text.get_rect().height / 2)))

        font = pg.font.Font(None, 60)
        text = font.render('START', True, (255, 255, 255))
        self.screen.blit(text, (400 - (text.get_rect().width / 2), 500 - (text.get_rect().height / 2)))

        for i in range(3):
            car = pg.sprite.Sprite()
            car.image = load_img('race/cars', constants.CARS_FOR_START[i])
            car.image = pg.transform.scale(car.image, (100, 100))
            car.rect = car.image.get_rect()
            car.rect.x = 125 + (225 * i)
            car.rect.y = 250
            starts.add(car)
        starts.draw(self.screen)

    def click(self, x, y):
        font = pg.font.Font(None, 30)
        state = font.render('selected', True, (255, 255, 255))
        if 125 <= x <= 225 and 250 <= y <= 350:
            self.chosen_car = constants.CARS_FOR_START[0]
            self.screen.blit(state, (175 - (state.get_rect().width / 2), 375))
        elif 350 <= x <= 450 and 250 <= y <= 350:
            self.chosen_car = constants.CARS_FOR_START[1]
            self.screen.blit(state, (400 - (state.get_rect().width / 2), 375))
        elif 575 <= x <= 675 and 250 <= y <= 350:
            self.chosen_car = constants.CARS_FOR_START[2]
            self.screen.blit(state, (625 - (state.get_rect().width / 2), 375))
        elif 333.5 <= x <= 466.5 and 479.5 <= y <= 520.5:
            self.starting = False
            Race(self.chosen_car)

    def glow(self, x, y):
        if 125 <= x <= 225 and 250 <= y <= 350:
            pg.draw.rect(self.screen, (255, 255, 255), (125, 250, 100, 100), 1)
        elif 350 <= x <= 450 and 250 <= y <= 350:
            pg.draw.rect(self.screen, (255, 255, 255), (350, 250, 100, 100), 1)
        elif 575 <= x <= 675 and 250 <= y <= 350:
            pg.draw.rect(self.screen, (255, 255, 255), (575, 250, 100, 100), 1)
        elif 333.5 <= x <= 466.5 and 479.5 <= y <= 520.5:
            pg.draw.rect(self.screen, (255, 255, 255), (323.5, 469.5, 153, 61), 1)
        else:
            self.interface()


if __name__ == '__main__':
    Start()
    pg.quit()
        
