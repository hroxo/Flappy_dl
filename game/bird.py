# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bird.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42porto.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 13:15:19 by hroxo             #+#    #+#              #
#    Updated: 2025/11/19 18:01:01 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame


class Birdy:
    def __init__(self, x, y, bird_img="./game/contents/bird.png"):
        self.x = x
        self.y = y
        self.bird_img = bird_img
        self.bird_img = pygame.image.load(self.bird_img).convert_alpha()
        self.bird_img = pygame.transform.scale(self.bird_img, (self.x / 20, self.y / 20))
