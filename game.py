#! /usr/bin/python3
import pygame
from loader.load_json_settings import load_setting
from view.render_manager import RenderManager
from controller.event_manager import EventManager


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
        self.renderer = RenderManager(self.screen, settings['renderSettings'])
        self.event_manager = EventManager()

    def run(self):
        self.event_manager.add(pygame.QUIT, self.exit)
        self.running = True
        idx = 0
        while self.running:
            self.renderer.render()
            self.event_manager.event()

    def exit(self):
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.run()
