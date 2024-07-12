####################載入套件######################
import pygame
import sys
import os
from pygame.locals import *

###################初始化設定########################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
######################載入圖片#########################
# 載入背景圖片
img_bg = pygame.image.load("image/space.png")
# 載入飛船圖片
img_sship = [
    pygame.image.load("image/fighter_M.png"),
    pygame.image.load("image/fighter_L.png"),
    pygame.image.load("image/fighter_R.png"),
]
# 載入飛船火焰
img_burn = pygame.image.load("image/starship_burner.png")
#####################遊戲視窗設定######################
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0


#####################定義函式區#######################
def roll_bg():
    """捲動背景"""
    global roll_y
    roll_y = (roll_y + 20) % bg_y
    screen.blit(img_bg, [0, roll_y - bg_y])
    screen.blit(img_bg, [0, roll_y])


def move_sship():
    """移動飛船"""
    global ss_x, ss_y, ss_wh, ss_hh, ss_img, burn_shift
    key = pygame.key.get_pressed()
    ss_img = img_sship[0]
    if key[pygame.K_UP]:
        ss_y -= 20
    if key[pygame.K_DOWN]:
        ss_y += 20
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        ss_img = img_sship[2]
        ss_x += 20
    ss_hh = ss_img.get_height() / 2
    ss_wh = ss_img.get_width() / 2
    if ss_y < ss_hh:
        ss_y = ss_hh
    if ss_y > bg_y - ss_hh:
        ss_y = bg_y - ss_hh
    if ss_x < ss_wh:
        ss_x = ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh
    burn_shift = (burn_shift + 2) % 6  # 飛船火焰的位移
    screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])  # 飛船火焰
    screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


####################玩家設定######################
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = img_sship[0]
burn_shift = 0  # 飛船火焰的位移
burn_w, burn_h = img_burn.get_rect().size  # 飛船火焰的寬度與高度
burn_shirt = 0
burn_w, burn_h = img_burn.get_rect().size
#####################主程式#######################
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F1:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen = pygame.display.set_mode(bg_size)
    roll_bg()
    move_sship()
    pygame.display.update()
