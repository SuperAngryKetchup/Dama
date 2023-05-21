import pygame

"""
ide lehet felvenni azon értékeket, amelyek az egész kódban fixek
"""

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (175, 50, 0) # jatekos szine
WHITE = (255, 255, 255) # szamitogep szine
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('kepek/crown.png'), (44, 25))
pcwins = pygame.transform.scale(pygame.image.load('kepek/computer wins.png'), (WIDTH, HEIGHT))
playerwins = pygame.transform.scale(pygame.image.load('kepek/user wins.png'), (WIDTH, HEIGHT))
player1wins = pygame.transform.scale(pygame.image.load('kepek/player1wins.png'), (WIDTH, HEIGHT))
player2wins = pygame.transform.scale(pygame.image.load('kepek/player2wins.png'), (WIDTH, HEIGHT))
