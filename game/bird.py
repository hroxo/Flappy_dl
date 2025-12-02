# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bird.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42porto.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 13:15:19 by hroxo             #+#    #+#              #
#    Updated: 2025/11/26 17:33:25 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame


class Birdy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        """"pygame Data"""
        raw_image = pygame.image.load("./game/contents/bird.png").convert_alpha()
        self.image = pygame.transform.scale(raw_image, (40, 30))
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
    def draw(self, screen):
        screen.blit(self.image, self.rect)
