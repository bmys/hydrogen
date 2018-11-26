import pygame
from loader.load_json_settings import load_setting
from view.render_manager import RenderManager


class Game:
    def __init__(self):
        # load settings
        settings = load_setting('settings.json')

        window_size = settings['windowSize']
        window_size = window_size['width'], window_size['height']
        title = settings['windowTitle']

        # start game
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(window_size)
        self.running = False
        self.render = RenderManager(self.screen, settings['renderSettings'])

    def run(self):
        self.running = True
        idx = 0
        while self.running:
            self.render.render()
            idx += 1
            if idx == 4000:
                return


if __name__ == '__main__':
    game = Game()
    game.run()
