import pygame, sys, time
from pygame.locals import *
import os

pygame.init()
mainClock = pygame.time.Clock()

W = 1280
H = 720

Surface = pygame.display.set_mode((W,H), 0, 32)
pygame.display.set_caption('Python Menus')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

game = True
mouse_pos = (0,0)
mouse_click = (0,0)
text1_bool = False
text2_bool = False
text_next_bool = False
text3_bool = False
text4_bool = False
output = '?'
n = 0

actor_files = []
i = 0

while game == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEMOTION:
            mouse_pos = event.pos
        if event.type == MOUSEBUTTONUP:
            mouse_click = event.pos

    Surface.fill(BLACK)
    color = WHITE
    Font = pygame.font.SysFont('arial', 25)
    if text1_bool:
        color = RED
    text = Font.render('Rating-Genre',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W/12,H/6)
    if text_rect.collidepoint(mouse_click):
        output = '1'
        barIMG1 = pygame.image.load('pic/1.png')
        barIMG1 = pygame.transform.scale(barIMG1,(800,600))
        Surface.blit(barIMG1,(W/3,H/10))

    if text_rect.collidepoint(mouse_pos):
        text1_bool = True
    else:
        text1_bool = False
    Surface.blit(text, text_rect)

    color = WHITE
    if text2_bool:
        color = RED
    Font = pygame.font.SysFont('arial', 25)
    text = Font.render('Rating-Actor(1)',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W/12,H*2/6)
    if text_rect.collidepoint(mouse_click):
        output = '2'
        barIMG2 = pygame.image.load('pic/2-1.png')
        barIMG2 = pygame.transform.scale(barIMG2,(800,600))
        Surface.blit(barIMG2,(W/3,H/10))
    if text_rect.collidepoint(mouse_pos):
        text2_bool = True
    else:
        text2_bool = False
    Surface.blit(text, text_rect)

    color = WHITE
    if text3_bool:
        color = RED
    
    Font = pygame.font.SysFont('arial', 25)
    text = Font.render('Rating-Actor(2)',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W/12,H*3/6)
    if text_rect.collidepoint(mouse_click):
        output = '3'
        barIMG3 = pygame.image.load('pic/2-2.png')
        barIMG3 = pygame.transform.scale(barIMG3,(800,600))
        Surface.blit(barIMG3,(W/3,H/10))
    if text_rect.collidepoint(mouse_pos):
        text3_bool = True
    else:
        text3_bool = False
    Surface.blit(text, text_rect)

    
    color = WHITE
    if text4_bool:
        color = RED
    Font = pygame.font.SysFont('arial', 25)
    text = Font.render('Genre-Year-Count',True,color)
    text_rect = text.get_rect()
    text_rect.center = (W/12,H*4/6)
    if text_rect.collidepoint(mouse_click):
        output = '4'
        barIMG3 = pygame.image.load('pic/3.png')
        barIMG3 = pygame.transform.scale(barIMG3,(800,600))
        Surface.blit(barIMG3,(W/3,H/10))
    if text_rect.collidepoint(mouse_pos):
        text4_bool = True
    else:
        text4_bool = False
    Surface.blit(text, text_rect)


    Font = pygame.font.SysFont('arial', 40)
    text = Font.render(output,True,BLUE)
    text_rect = text.get_rect()
    text_rect.center = (W/10,H*4/5)
    Surface.blit(text, text_rect)



    pygame.display.flip()
    mainClock.tick(100000)