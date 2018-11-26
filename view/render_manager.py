from pygame import Surface
import pygame


class RenderManager:
    def __init__(self, screen: Surface, render_settings: dict):
        """
        Render manager is responsible for drawing on screen.
        Manage sprites etc.

        :param screen:
        :param render_settings:
        """

        self.screen = screen
        self.color = render_settings['backgroundColor']

    def render(self):
        self.screen.fill(self.color)
        pygame.display.flip()
