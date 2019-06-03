from pygame import Surface
import pygame
from collections import defaultdict
import weakref


class EventManager:
    """
         Event manager is responsible for operate event calls.

    """

    class KeyboardEvents:
        def __init__(self):
            # Event type, key code, events
            self.key_events = defaultdict(lambda: defaultdict(list))

        def add(self, event_type, key, delegate):
            weak_ref = weakref.ref(delegate)
            self.key_events[event_type][key].append(weak_ref)

        def remove(self, event_type, key, delegate):
            self.key_events[event_type][key].pop(delegate)

    def __init__(self):
        self.event_dict = defaultdict(list)

    def event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                for delegate in self.event_dict[event.key]:
                    delegate(event)
            else:
                for delegate in self.event_dict[event.type]:
                    delegate(event)

    def add(self, event, delegate):
        weak_ref = weakref.ref(delegate)
        self.event_dict[event].append(weak_ref)

    def remove(self, event):
        self.event_dict.pop(event)

    def is_active(self, event_type):
        return event_type in self.event_dict.keys()

    def is_blocked(self, event_type):
        return event_type in self.event_dict.keys()


def block(event_type):
    pygame.event.set_blocked(event_type)


def allow(event_type):
    pygame.event.set_allowed(event_type)
