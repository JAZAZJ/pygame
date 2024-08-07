######################匯入模組######################
import pygame
import sys
import os
import random
###################定義函式######################
def gophers_update():
    global tick, pos
    if tick > max_tick: # 每20次刷新變換一次
        new_pos = random.randint(0, 5) # 隨機0到5
        pos = pos6[new_pos] # 更新外部記錄的圓的位置
        tick = 0 # 重置計數器
    else: # 不刷新變換的時候
        tick += 1 # 增加計數器
    screen.blit(gophers, (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))
    screen.blit(gophers,(pos[0]-gophers.get_width()/2,pos[1]-gophers.get_height()/2)) # 使用隨機位置

def score_update():
    score_sur = score_font.render(str(score), False, RED) # 分數文字渲染
    screen.blit(score_sur, (10, 10)) # 將分數文字貼到視窗上

def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False

####################初始化######################
os.chdir(sys.path[0])
pygame.init()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0 # 計數器目前值
max_tick = 20 # 設定計數器最大值
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################
bg_x = 800
bg_y = 600
screen = pygame.display.set_mode([bg_x, bg_y]) # 設定窗口
pygame.display.set_caption("打地鼠")
######################背景物件######################
######################地鼠物件######################
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]] # 六個位置
# pos6 = [[200, 200], [300, 200], [400, 200], [200, 300], [300, 300], [400, 300]] 
# 模擬地鼠出現的位置
pos = pos6[0] # 外面記錄圓的位置
gophers = pygame.image.load("Gophers150.png") # 地鼠圖片
######################分數物件######################
score = 0 # 分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
######################滑鼠物件######################

######################循環偵測######################
while True:
    clock.tick(30) # 每秒執行30次
    mouse_pos = pygame.mouse.get_pos()
# 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50, pos[1] + 50):
                tick = max_tick + 1 # 立即刷新
                score += 1 # 分數加1
    screen.blit(bg, (0, 0)) # 貼上背景
    gophers_update() # 更新地鼠
    score_update() # 更新分數

    pygame.display.update()