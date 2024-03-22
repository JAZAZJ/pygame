###################匯入模組###################
import pygame
import sys
import os
import math
import random
###################初始化###################
os.chdir(sys.path[0])# 設定程式執行路徑
pygame.init()    # 啟動 Pygame
bg_img = "snow.jpg" 
bg = pygame.image.load(bg_img)
bg_x = bg.get_width() # 640
bg_y = bg.get_height() # 400
WHITE = (255,255,255)
BLACK = (0,0,0)
width = 640 #設定視窗寬度
height = 320
###################設定雪花基本參數#################
snow_list = []
for i in range(150):
    x_site = random.randrange(0,bg_x)
    y_site = random.randrange(-bg_y,-1)
    x_shift = random.randint(-1,1)
    radius = random.randint(2,6) 
    snow_list.append({"x_site": x_site,"y_site": y_site,"x_shift":x_shift,"radius":radius})
###################定義函式#################
def check_click(pos,x_min,y_min,x_max,y_max):
    print(pos[1],pos[0],x_min,y_min,x_max,y_max)
    x_match =(x_min < pos[0] <  x_max)
    y_match = (y_min < pos[1] <  y_max)
    if x_match and y_match:
        return True
    else:
        return False
def snow_fall():
    for snow in snow_list:
        global x_site,y_site,x_shift,radius
        pygame.draw.circle(screen,WHITE,(snow["x_site"],snow["y_site"]),snow["radius"])
        snow["x_site"] += snow["x_shift"]
        snow["y_site"] += snow["radius"]
        y_site += radius
        if snow["y_site"] > bg_y or snow["x_site"] > bg_x:
                snow["y_site"] = random.randint(-bg_y,-1)
                snow["x_site"] = random.randint(0,bg_x)
###################撥放音樂#####################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path) # 音樂載入程式
pygame.mixer.music.play() # 撥放音樂 
pygame.mixer.music.fadeout(600000) # 設定音樂撥放時
pygame.mixer.music.pause()
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

###################新增fps##################
clock = pygame.time.Clock()
###################循環偵測##################
paint = False # 畫布狀態
cnt = 0
while True:
    clock.tick(200)
    mouse_pot = pygame.mouse.get_pos()

    #取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果吃下[x]就選出 # 使用者按關閉鈕
            sys.exit() #離開遊戲
        if event.type == pygame.MOUSEBUTTONDOWN:  # 偵測滑鼠按下
            if check_click(mouse_pot,int(0),int(0),tit_w,tit_h):
                paint = not paint
    if cnt > 10:
        #當雪球落下10次後,改變下雪方向
        cnt = 0
        x_shift = random.randint(-40,100)
    else:
        cnt += 1
    screen.blit(bg,(0,0))
    screen.blit(title,(0,0))
    if paint:
        title = font.render("Start",True,BLACK)
        print(f"!!!!!!!!!!!!!!!!!!!1")
        pygame.mixer.music.unpause()
        snow_fall()
    else:
        title = font.render("Stop", True,BLACK)
        pygame.mixer.music.pause()
    # screen.blit(bg,(0,0))
    # screen.blit(title,(0,0))
    pygame.display.update()