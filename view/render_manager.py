from pygame import Surface

class RenderManager:
    def __init__(self, screen: Surface, render_settings: dict):
        '''
        Render manager is responsible for drawing on screen.
        Manage sprites etc.
        :param render_settings:
        '''
        self.screen = screen


