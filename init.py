import pygame
from loader.load_json_settings import load_setting

#load settings
settings = load_setting('settings.json')

print(settings)
window_size = settings['windowSize']
window_size = window_size['width'], window_size['height']
title = settings['windowTitle']

print(window_size)

pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode(window_size)
