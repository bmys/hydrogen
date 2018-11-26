from pygame import Surface
import pygame


class EventManager:
    def __init__(self, screen: Surface, render_settings: dict):
        """
        Event manager is responsible for operate event calls.

        :param screen:
        :param render_settings:
        """

        self.screen = screen
        self.color = render_settings['backgroundColor']

    def event(self):
        self.screen.fill(self.color)
        pygame.display.flip()
