# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 12:19:04 by hroxo             #+#    #+#              #
#    Updated: 2025/12/02 23:45:48 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from pygame.constants import K_SPACE, K_q
from .bird import Birdy
from .pipes import Pipes

def draw_components(screen, bird, clock, x, y, pipe):

    if clock == 0:
        pipe.append(Pipes(x, y))

    for i in range(len(pipe)):
        pipe[i].update()

    if clock != 0 and clock % 100 == 0:
        """A killer for the pipes that are no longer on screen"""
        if pipe[0].top_rect.right < 0:
            pipe.pop(0)
        """Create a new pipe to replace the older"""
        pipe.append(Pipes(x, y))

    """A handy function to draw each element to the screen"""

    for i in range(len(pipe)):
        pipe[i].draw(screen)

    bird.draw(screen)

def game_over(bird, pipes, score):

    game_running = True

    if not bird.rect.bottom >= 0 and bird.rect.top <= 0:
        game_running = False
        return game_running, score
    for pipe in pipes:

        if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
            game_running = False

        if not pipe.passed and bird.rect.left > pipe.top_rect.right:
            score += 1
            pipe.passed = True

    return game_running, score


pygame.init()

width = 800
height = 800

screen = pygame.display.set_mode((width, height))

img = pygame.image.load("./game/contents/background.png")
clock = pygame.time.Clock()
img = pygame.transform.scale(img, (width ,height))
bird = Birdy(height / 3, width / 3)

pipe = []

running = True

time = 0
score = 0
status = True

while running:

    screen.blit(img, (0, 0))
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False
            else:
                bird.jump()
        elif event.type == pygame.QUIT: 
            running = False
    bird.move()
    draw_components(screen, bird, time, width, height, pipe)
    status, score = game_over(bird, pipe, score)
    if not status:
        running = False

    pygame.display.flip()
    time += 1
    clock.tick(60)  # limits FPS to 60

print(score)
pygame.quit()
