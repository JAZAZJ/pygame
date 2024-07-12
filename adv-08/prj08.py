def move_dinosaur():
    global ds_y,jumpstate,jumpvalue,ds_index
    if jumpstate:
        if ds_y>=LIMIT_LOW:
            jumpvalue=-jumpheight
        if ds_y<=0:
            jumpvalue=jumpheight
        ds_y+=jumpvalue
        jumpvalue+=1
        if ds_y>=LIMIT_LOW:
            jumpstate=False
            ds_y=LIMIT_LOW
    ds_index=(ds_index-1)% len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index],(ds_x,ds_y)) 
#######################匯入模組#####################
import pygame
import sys
import os
from pygame.locals import *
#######################初始化#######################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW=140
clock=pygame.time.Clock()
red=(255,0,0)
######################載入圖片物件##################
img=pygame.image.load('image/bg.png')
img_dinosaur=[
    pygame.image.load('image/小恐龍1.png'),
    pygame.image.load('image/小恐龍2.png'),
]
img_cati=pygame.image.load('image/cacti.png')
bg_x=img.get_width()
bg_y=img.get_height()
bg_roll_x=0
#####################分數物件#######################
score=0
typeface=pygame.font.get_default_font()
score_font=pygame.font.Font(typeface,36)
#####################恐龍物件#######################
ds_x=50
ds_y=LIMIT_LOW
ds_index=0
jumpstate=False
jumpvalue=0
jumpheight=13
#####################仙人掌物件#######################
cacti_x=bg_x-100
cacti_y=LIMIT_LOW
cacti_shift=10
######################建立視窗######################
screen=pygame.display.set_mode([bg_x,bg_y])
pygame.display.set_caption('Dinosaur')
######################定義函式######################
def bg_update():
    global bg_roll_x
    bg_roll_x=(bg_roll_x-10)%bg_x
    screen.blit(img,(bg_roll_x-bg_x,0))
    screen.blit(img,(bg_roll_x,0))
def move_dinosaur():
    global ds_y,jumpstate,jumpvalue,ds_index
    if jumpstate:
        if ds_y>=LIMIT_LOW:
            jumpvalue=-jumpheight
        if ds_y<=0:
            jumpvalue=jumpheight
            ds_y+=jumpvalue
            jumpvalue+=1
        if ds_y>=LIMIT_LOW:
            jumpstate=False
            ds_y=LIMIT_LOW
    ds_index=(ds_index-1)% len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index],(ds_x,ds_y))
    if  cacti_x <= 0:
        score += 1
def move_cacti():
    """移動仙人掌"""
    global cacti_x,score
    cactsi_x=(cacti_x-cacti_shift)%(bg_x-100)
    screen.blit(img_cati,(cacti_x,cacti_y))
    if cacti_x <= 0:
        score += 1
def score_update():
    score_sur=score_font.render(str(score),True,red)
    screen.blit(score_sur,[10,10])
######################循環偵測######################
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE and ds_y<=LIMIT_LOW:
                jumpstate=True
    bg_update()
    move_dinosaur()
    score_update()
    move_cacti()
    pygame.display.update()