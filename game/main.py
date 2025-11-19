# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 12:19:04 by hroxo             #+#    #+#              #
#    Updated: 2025/11/19 13:32:11 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
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
    
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("blue")
            screen.blit(self.img, (0, 0))

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()


tab = DrawScreen()
tab.create_screen()
