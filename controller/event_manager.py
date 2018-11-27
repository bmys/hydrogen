from pygame import Surface
import pygame
from collections import defaultdict


class EventManager:
    def __init__(self):
        """
        Event manager is responsible for operate event calls.

        :param screen:
        :param render_settings:
        """

        self.event_dict = defaultdict(list)

    def event(self):
        events = pygame.event.get()
        for event in events:
            for delegate in self.event_dict[event.type]:
                delegate()

    def add(self, event, delegate):
        self.event_dict[event].append(delegate)

