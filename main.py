from settings import *
from visa import *
import pygame
pygame.init()
def draw_field():
    for i, tile in enumerate (field):
        if tile == EMPTY:
            pygame.draw.rect(screen,(255,255,255),((i%FIELD_WIDTH)*TILE_SIZE,(i//FIELD_WIDTH)*TILE_SIZE,TILE_SIZE,TILE_SIZE),)

fon =(29, 21, 46)
person = (162,150,186)

screen =pygame.display.set_mode(RES)
clock=pygame.time.Clock()
gengar = {
    "x":0 ,
    "y":0
}
run= True
while run :
    pygame.display.flip()
    clock.tick(FPS)
    screen.fill((0,0,0))
    draw_field()
    pygame.draw.line(screen,person,(gengar["x"],gengar["y"]),(gengar["x"]+50,gengar["y"]+50),20)
    keys= pygame.key.get_pressed()
    if keys[pygame.K_d]:
        gengar["x"]+=10
    if keys[pygame.K_a]:
        gengar["x"]-=10
    if keys[pygame.K_s]:
        gengar["y"]+=10
    if keys[pygame.K_w]:
        gengar["y"]-=10
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
pygame.quit()