# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 12:19:04 by hroxo             #+#    #+#              #
#    Updated: 2025/11/26 18:37:21 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from pygame.constants import K_SPACE, K_q
from .bird import Birdy
from .pipes import Pipes

class DrawScreen:
    def __init__(self, height=800, width=800):
        self.height = height
        self.width = width

    def create_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))

        self.img = pygame.image.load("./game/contents/background.png")
        clock = pygame.time.Clock()
        self.img = pygame.transform.scale(self.img, (self.width ,self.height))
        self.bird = Birdy(self.height / 3, self.width / 3)
        self.pipes = Pipes(self.height, self.width)
        running = True
        while running:
            screen.blit(self.img, (0, 0))
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        running = False
                    else:
                        self.bird.jump()
                elif event.type == pygame.QUIT: 
                    running = False
            self.bird.move()
            self.pipes. update()
            self.bird.draw(screen)
            self.pipes.draw(screen)
            pygame.display.flip()
            clock.tick(60)  # limits FPS to 60

        pygame.quit()


tab = DrawScreen()
tab.create_screen()
