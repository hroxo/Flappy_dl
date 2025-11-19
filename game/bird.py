# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bird.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42porto.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 13:15:19 by hroxo             #+#    #+#              #
#    Updated: 2025/11/19 15:14:21 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame

class Birdy:
    def __init__(self, bird_img="./game/contents/bird.png"):
        self.bird_img = bird_img
        self.bird_img = pygame.image.load(self.bird_img).convert_alpha()

