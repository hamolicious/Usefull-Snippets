"""
A fixed framerate pygame boiler plate code
"""

import pygame

#region pygame init
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 30

#endregion

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(0)
    
    mouse_pos   = pygame.mouse.get_position()
    mouse_press = pygame.mouse.get_pressed()
    key_press   = pygame.key.get_pressed()

    # -- Code Here -- #

    pygame.display.update()
    clock.tick(fps)
