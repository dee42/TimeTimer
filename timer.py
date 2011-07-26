#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys, pygame
pygame.init()

size = width, height = 320, 320
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

screen = pygame.display.set_mode(size)

# Create 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 in black with background white
font = pygame.font.Font(None, 20)
numbers = [font.render(str(num), True, black, white) for num in range(0, 60, 5)]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Draw the clock
    screen.fill(black)
    # White circle, filled
    # Black inner circle
    # Mark 60 lines in black on the Circle, bigger ones on the 5 minute intervals
    # Place the text on the correct lines
    # Draw the arc in red on the clock
    pygame.display.flip()
