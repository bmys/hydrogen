from pygame import Surface
import pygame
from collections import defaultdict


class EventManager:
    def __init__(self):
        """
        Event manager is responsible for operate event calls.

        """

        self.event_dict = defaultdict(list)

    def event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                for delegate in self.event_dict[event.key]:
                    delegate()
            else:
                for delegate in self.event_dict[event.type]:
                    delegate()

    def add(self, event, delegate):
        self.event_dict[event].append(delegate)

