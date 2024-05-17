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
LIMIT_LOW = 140 # 地面高度
PTERA_LIMIT_LOW = 110 # 翼龍高度
clock = pygame.time.Clock()
RED = (255, 0, 0) # 紅色
######################載入圖片物件##################
img=pygame.image.load('image/bg.png')
img_dinosaur=[
    pygame.image.load('image/小恐龍1.png'),
    pygame.image.load('image/小恐龍2.png'),
]
# img_cati=pygame.image.load('image/cacti.png')
img_ptera = [pygame.image.load("image/翼龍飛飛1.png"),pygame.image.load("image/翼龍飛飛2.png")]
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
ptera_x=bg_x-100
ptera_y=LIMIT_LOW
ptera_shift=10
####################翼龍物件#######################
ptera_x = bg_x- 100 # 障礙物x位置
ptera_y = PTERA_LIMIT_LOW # 障礙物y位置
ptera_index = 0 # 翼龍圖片編號
ptera_shift = 10 # 翼龍移動量
ptera_center_x = ptera_x + img_ptera[0].get_width() / 2 # 翼龍中心x位置
ptera_center_y = ptera_y + img_ptera[0].get_height() / 2 # 翼龍中心y位置
# 翼龍偵測半徑
ptera_detect_r = max(img_ptera[0].get_width(), img_ptera[0].get_height()) / 2 - 1
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
    if  ptera_x <= 0:
        # score += 1
        def move_ptera():
            global ptera_x,score
            ptera_x=(ptera_x)%(bg_x-100)
            screen.blit(img_ptera,(ptera_x))
            if ptera_x <= 0:
                score += 1
def score_update():
    score_sur=score_font.render(str(score),True,RED)
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
    # move_cacti()
    pygame.display.update()