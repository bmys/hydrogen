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
        event = pygame.event.get()
        for subscriber in self.event_dict[event]:
            subscriber.event(event)

    def add(self, event, delegate):
        self.event_dict[event].append(delegate)
