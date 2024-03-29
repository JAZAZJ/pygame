###################匯入模組###################
import pygame
import sys
import os
import math
###################定義函式#################
def check_click(pos,x_min,y_min,x_max,y_max):
    print(pos[0],pos[1],x_min,y_min,x_max,y_max)
    x_match =(x_min < pos[0] <  x_max)
    y_match = (y_min < pos[1] <  y_max)
    if x_match and y_match:
        return True
    else:
        return False
###################初始化###################
os.chdir(sys.path[0])# 設定程式執行路徑
pygame.init()    # 啟動 Pygame
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width() # 640
bg_y = bg.get_height() # 400
WHTITE = (255,255,255)
BLACK = (0,0,0)
width = 640 #設定視窗寬度
height = 320

###################撥放音樂#####################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path) # 音樂載入程式
pygame.mixer.music.play() # 撥放音樂 
pygame.mixer.music.fadeout(60000) # 設定音樂撥放時
# pygame.mixer.music.pause
# pygame.mixer.music.unpause
###################設定文字#####################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface,24)
title = font.render("start",True,(0,0,0))
tit_w = title.get_width()
tit_h = title.get_height()
###################建立視窗及物件###################
screen = pygame.display.set_mode((bg_x,bg_y))
pygame.display.set_caption("Snow")
# 設定視窗大小
screen = pygame.display.set_mode((width,height))
# 設定視窗標題
pygame.display.set_caption("My game")
# ###################建立畫布##################
# #建立畫布
# bg = pygame.Surface((width,height))
# # 畫布為白色(R,G,B)
# bg.fill((255,255,255))
###################設定雪花基本參數#################
###################新增fps##################
clock = pygame.time.Clock()
###################循環偵測##################
paint = False # 畫布狀態
while True:
    clock.tick(20)
    mouse_pot = pygame.mouse.get_pos()

    #取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果吃下[x]就選出 # 使用者按關閉鈕
            sys.exit() #離開遊戲
        if event.type == pygame.MOUSEBUTTONDOWN:  # 偵測滑鼠按下
            if check_click(mouse_pot,int(0),int(0),tit_w,tit_h):
                paint = not paint
    if paint:
        title = font.render("Start",True,BLACK)
    else:
        title = font.render("Stop", True,BLACK)
    screen.blit(bg,(0,0))
    screen.blit(title,(0,0))
    pygame.display.update()