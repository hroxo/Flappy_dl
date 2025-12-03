# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hroxo <hroxo@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/19 12:19:04 by hroxo             #+#    #+#              #
#    Updated: 2025/12/03 22:29:54 by hroxo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from pygame.constants import K_SPACE, K_q
from .bird import Birdy
from .pipes import Pipes
from .engine import Hooks

def draw_components(screen, bird, clock, x, y, pipes):

    if clock == 0:
        pipes.append(Pipes(x, y))

    for pipe in pipes:
        pipe.update(bird.x)

    if clock != 0 and clock % 100 == 0:
        """A killer for the pipes that are no longer on screen"""
        if pipes[0].top_rect.right < 0:
            pipes.pop(0)
        """Create a new pipe to replace the older"""
        pipes.append(Pipes(x, y))

    """A handy function to draw each element to the screen"""

    for pipe in pipes:
        pipe.draw(screen)

    bird.draw(screen)

def game_over(bird, pipes, score):

    game_running = True

    if bird.rect.top <= 0 or bird.rect.bottom >= 800:
        game_running = False
        return game_running, score
    for pipe in pipes:

        if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
            game_running = False

        if pipe.passed == True and pipe.scored == False:
            pipe.scored = True 
            score += 1

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
kill = False

input_handler = Hooks()

while running:

    screen.blit(img, (0, 0))
    pygame.event.pump()
    
    action = input_handler.listen_events()
    
    if "quit" in action:
        running = False

    if "jump" in action:
        bird.jump()
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == K_q:
    #             running = False
    #         else:
    #             bird.jump()
    #     elif event.type == pygame.QUIT:
    #         running = False
    #         kill = True
    bird.move()
    draw_components(screen, bird, time, width, height, pipe)
    status, score = game_over(bird, pipe, score)
    if not status:
        running = False

    pygame.display.flip()
    time += 1
    clock.tick(60)  # limits FPS to 60

print(f"\tNEW SCORE\n\n\t{score}")

while kill == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                kill = True
        elif event.type == pygame.QUIT:
            kill = True

pygame.quit()
