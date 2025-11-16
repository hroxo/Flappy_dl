# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tab.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42porto.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/16 23:07:20 by hroxo             #+#    #+#              #
#    Updated: 2025/11/16 23:23:54 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame

class screen:
    def __init__(self, height=800, width=800):
        self.height = height
        self.width = width
    def create_screen(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("blue")

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()


tab = screen(720, 1280)
tab.create_screen()
