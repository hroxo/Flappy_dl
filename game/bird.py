# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bird.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42porto.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 13:15:19 by hroxo             #+#    #+#              #
#    Updated: 2025/12/02 23:21:01 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame


class Birdy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        """pygame Data"""

        raw_image = pygame.image.load("./game/contents/bird.png").convert_alpha()
        self.image_original = pygame.transform.scale(raw_image, (45, 35))
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        """Data to scaler components"""

        self.vel = 0
        self.gravity = 0.5
        self.lift = -8

    def jump(self):

        """Aplica-se o impulso o passaro salta para cima"""

        self.vel = self.lift

    def move(self):

        self.y += self.vel
        self.vel += self.gravity

        self.rect.centery = int(self.y)
       
        rotation = self.vel * -3
        if rotation > 30:
            self.image = pygame.transform.rotate(self.image_original, 30) 
        elif rotation < -30:
            self.image = pygame.transform.rotate(self.image_original, -30) 
        else:
            self.image = pygame.transform.rotate(self.image_original, rotation) 

    def happy_bird(self):

        self.image = pygame.transform.rotate(self.image_original, 360)

    def draw(self, screen):

        screen.blit(self.image, self.rect)
