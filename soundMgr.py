# Networking manager. Manage networking. Create networking threads, find clients/servers, sync entities

class SoundMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
        
      import pygame
      from pygame import *
      import sys

      pygame.init()
      pygame.mixer.init()
      Background = pygame.mixer.Sound("mars.ogg")
      Background.play(loops = 5)

    def tick(self, dt):
        pass

    def stop(self):
        pass
