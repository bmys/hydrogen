from pygame import Surface
import pygame
from collections import defaultdict


class EventManager:
    def __init__(self, screen: Surface, render_settings: dict):
        """
        Event manager is responsible for operate event calls.

        :param screen:
        :param render_settings:
        """

        self.screen = screen
        self.color = render_settings['backgroundColor']
        self.event_dict = defaultdict(list)

    def event(self):
        event = pygame.event.get()
        for subscriber in self.event_dict[event]:
            subscriber.event(event)
