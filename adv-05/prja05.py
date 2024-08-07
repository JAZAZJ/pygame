######################匯入模組######################
import pygame
import sys
import os
import random
###################定義函式######################
def gophers_update():
    global tick, pos,times
    if tick > max_tick: # 每20次刷新變換一次
        new_pos = random.randint(0, 5) # 隨機0到5
        pos = pos6[new_pos] # 更新外部記錄的圓的位置
        tick = 0 # 重置計數器
        times += 1
    else: # 不刷新變換的時候
        tick += 1 # 增加計數器
    screen.blit(gophers, (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))
    screen.blit(gophers,(pos[0]-gophers.get_width()/2,pos[1]-gophers.get_height()/2)) # 使用隨機位置
def times_update():
    """更新次數"""
    times_sur = times_font.render(str(times),True,RED)
    screen.blit(times_sur,(bg_x - times_sur.get_width()-10,10))
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
def game_over():
    """遊戲結束"""
    screen.fill(BLACK)
    end_sur = score_font.render(f"Game Over~Your Score is:{score}",False,RED)
    screen.blit(end_sur,(bg_x / 2 - end_sur.get_width() / 2,bg_y / 2 - end_sur.get_height() / 2))
def mouse_update():
    global hammer,hammer_tick
    if hammer == ham1:
        hammer = ham2
        hammer_tick = 0
    else:
        hammer_tick += 1
    screen.blit(hammer,(mouse_pos[0]-15,mouse_pos[1]))
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
######################次數物件#######################
times = 0
times_max = 10
typeface = pygame.font.get_default_font()
times_font = pygame.font.Font(typeface,24)
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
pygame.mouse.set_visible(False) # 隱藏滑鼠
ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
hammer = ham2 # 設定目前要顯示的鎚子圖片
hammer_tick = 0 # 計數器目前值
hammer_max_tick = 5 # 設定計數器最大值

######################循環偵測######################
while True:
    clock.tick(30) # 每秒執行30次
    mouse_pos = pygame.mouse.get_pos()
# 取得事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50, pos[1] + 50):
                tick = max_tick + 1 # 立即刷新
                score += 1 # 分數加1
    if times >= times_max:
        game_over()
    else :
        screen.blit(bg, (0, 0)) # 貼上背景
        gophers_update() # 更新地鼠
        score_update() # 更新分數
        times_update() # 更新次數
        mouse_update() # 更新滑鼠
    pygame.display.update()