# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary scrpit file
"""
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

dino_rect = pygame.Rect(100, 250, 64, 64)
#Code for cactus_rect here as mentioned in screen
ground_rect = pygame.Rect(0, 330, 1200, 2)
cactus_rect = pygame.Rect(1100, 300, 32, 32)
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           

    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cactus_rect)  # Replace the "--" in the code with the relevant information
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)

    pygame.display.update()
    
    
    
