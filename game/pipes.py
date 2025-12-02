# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pipes.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42porto.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/26 18:09:16 by hroxo             #+#    #+#              #
#    Updated: 2025/11/26 18:39:17 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
import random

class Pipes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.gap_size = 200
        self.min_y = 100
        self.max_y = y - (self.gap_size + self.min_y)

        self.gap_y = random.randint(self.min_y, self.max_y)

        raw_image = pygame.image.load("./game/contents/pipe.png").convert_alpha()
        scaled_image = pygame.transform.scale(raw_image, (100, 800))

        self.top_pipe = pygame.transform.flip(scaled_image, False, True)
        self.bottom_pipe = scaled_image
        
        self.top_rect = self.top_pipe.get_rect()
        self.top_rect.left = self.x
        self.top_rect.bottom = self.gap_y

        self.bottom_rect = self.bottom_pipe.get_rect()
        self.bottom_rect.left = self.x
        self.bottom_rect.bottom = self.gap_y + self.gap_size
   
        self.vel = -2

    def update(self):
        self.x += self.vel

        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)
    def draw(self, screen):
        screen.blit(self.top_pipe, self.top_rect)
        screen.blit(self.bottom_pipe, self.bottom_rect)
