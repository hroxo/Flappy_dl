
import pygame
from pygame.constants import K_SPACE, K_q, K_r

class Hooks:

    def __init__(self):
        self.key_map = {
            pygame.K_SPACE: "jump",
            pygame.K_UP: "jump",
            K_q: "quit",
            pygame.K_ESCAPE: "quit",
            pygame.QUIT: "quit",
            K_r: "replay"
        }

    def listen_events(self):

        actions = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actions.append("quit")
            
            elif event.type == pygame.KEYDOWN:
                if event.key in self.key_map:
                    actions.append(self.key_map[event.key])

        return actions

