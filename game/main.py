# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 12:19:04 by hroxo             #+#    #+#              #
#    Updated: 2025/11/19 18:01:41 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from pygame.constants import K_SPACE, K_q
from .bird import Birdy

class DrawScreen:
    def __init__(self, height=800, width=800, img="./game/contents/background.png"):
        self.height = height
        self.width = width
        self.img = img
    def create_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))

        self.img = pygame.image.load(self.img)
        self.img = pygame.transform.scale(self.img, (self.width ,self.height))
        clock = pygame.time.Clock()
        birdimg = Birdy(self.width, self.height)
        running = True
        i = 0
        while running:
            screen.blit(self.img, (0, 0))
            screen.blit(birdimg.bird_img, (self.width / 3, i))
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        running = False
                    else:
                        i -= 200
                elif event.type == pygame.QUIT: 
                    running = False
            pygame.display.flip()
            i += 10
            clock.tick(60)  # limits FPS to 60

        pygame.quit()


tab = DrawScreen()
tab.create_screen()
