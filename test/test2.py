######################匯入模組######################
import pygame
import sys
######################初始化######################
pygame.init() # 啟動 Pygame
width = 640 # 設定視窗寬度
height = 320 # 設定視窗高度
######################建立視窗及物件######################
# 設定視窗大小
screen = pygame.display.set_mode((width, height))
# 設定視窗標題
pygame.display.set_caption("My Game")
######################建立畫布######################
 # 建立畫布
bg = pygame.Surface((width, height))
# 畫布為白色(R, G, B)
bg.fill((255, 255, 255))
######################循環偵測######################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 如果按下 [X] 就退出
            sys.exit() # 離開遊戲
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click!!")
            print(pygame.mouse.get_pos()) # 取得滑鼠座標
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pos() # 取得滑鼠座標
    x, y = pygame.mouse.get_pos() # 存出座標
            # 繪製畫布於視窗左上角
     # 繪製畫布於視窗左上角
    screen.blit(bg, (0, 0))
    # 更新視窗
    pygame.display.update()
    ######################繪製圖形######################
    pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
    pygame.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)
    pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
    pygame.draw.ellipse(bg, (255, 0, 0), [130, 160, 60, 35], 5)
    pygame.draw.ellipse(bg, (255, 0, 0), [400, 160, 60, 35], 5)
    pygame.draw.line(bg, (255, 0, 255), (280, 220), (320, 220), 3)