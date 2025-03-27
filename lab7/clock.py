import pygame 
import time
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

leftarm = pygame.image.load("images/leftarm.png")
rightarm = pygame.image.load("images/rightarm.png")
mainclock = pygame.transform.scale(pygame.image.load("mickeyclock.jpeg"), (800, 600))
done = False

pygame.quit()