import os
import pygame

WIN_WIDTH = 500
WIN_HEIGHT = 700

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
#IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_BACKGROUND = pygame.image.load(os.path.join('imgs', 'bgg.png'))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

#
# IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load('./imgs/pipe.png'))
# IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load('./imgs/base.png'))
# IMAGEM_BACKGROUND = pygame.image.load('./imgs/bgg.png')
# IMAGEM_PASSARO = [
#     pygame.transform.scale2x(pygame.image.load('./imgs/bird1.png')),
#     pygame.transform.scale2x(pygame.image.load('./imgs/bird2.png')),
#     pygame.transform.scale2x(pygame.image.load('./imgs/bird3.png'))
# ]


# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# W
WIN_WIDTH = 500
WIN_HEIGHT = 700