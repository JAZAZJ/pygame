# ######################匯入模組######################
# import pygame
# import sys
# ####################定義函式######################
# def check_click(pos, x_min, y_min, x_max, y_max):
#     """判斷滑鼠是否點擊在指定的區域內"""
#     x_match = x_min < pos[0] < x_max
#     y_match = y_min < pos[1] < y_max
#     if x_match and y_match:
#         return True
#     else:
#         return False
# ######################初始化######################
# pygame.init() # 啟動 Pygame
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# width = 640
# height = 320
# ######################建立視窗及物件######################
# # 設定視窗大小
# screen = pygame.display.set_mode((width, height))
# # 設定視窗標題
# pygame.display.set_caption("My Game")
# ######################建立畫布######################
#  # 建立畫布
# bg = pygame.Surface((width, height))
# # 畫布為白色(R, G, B)
# bg.fill((255, 255, 255))
# ####################設定文字######################
# # 取得系統字體
# typeface = pygame.font.get_default_font()
#  # 設定字體和大小
# font = pygame.font.Font(typeface, 24)
#  # 設定文字參數: 文字內容, 是否開啟反鋸齒, 文字顏色, 背景顏色
# title = font.render("Start", True, (0, 0, 0))
#  # 取得文字寬度
# tit_w = title.get_width()
#  # 取得文字高度
# tit_h = title.get_height()
# ######################循環偵測######################
# paint = False # 畫布狀態
# while True:
#     screen.blit(bg, (0, 0))
#     mouse_pos = pygame.mouse.get_pos()
#     print(mouse_pos)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: # 如果按下 [X] 就退出
#             sys.exit() # 離開遊戲
#         if event.type == pygame.MOUSEBUTTONDOWN:
#              if check_click(mouse_pos, 0, 0, tit_w, tit_h):
#                 paint = not paint # 當點擊時，切換畫布狀態
#         print("click!!")
#         print(pygame.mouse.get_pos()) # 取得滑鼠座標
#         if event.type == pygame.MOUSEBUTTONDOWN:
            
#             pygame.mouse.get_pos() # 取得滑鼠座標
#     x, y = pygame.mouse.get_pos() # 存出座標
#             # 繪製畫布於視窗左上角
#      # 繪製畫布於視窗左上角
#     screen.blit(bg, (0, 0))# 更新視窗
#     screen.blit(title, (0, 0))
#     if paint:
#         pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
#         pygame.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)
#         pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
#         pygame.draw.ellipse(bg, (255, 0, 0), [130, 160, 60, 35], 5)
#         pygame.draw.ellipse(bg, (255, 0, 0), [400, 160, 60, 35], 5)
#         pygame.draw.line(bg, (255, 0, 255), (280, 220), (320, 220), 3)
#     else:
#         bg.fill(WHITE) # 使用白色填充背景
#     screen.blit(title, (0, 0)) # 將標題圖像繪製在螢幕的 (0, 0) 位置
#     pygame.display.update()
#         ######################繪製圖形######################
#     pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
#     pygame.draw.circle(bg, (0, 0, 255), (400, 100), 30, 0)
#     pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
#     pygame.draw.ellipse(bg, (255, 0, 0), [130, 160, 60, 35], 5)
#     pygame.draw.ellipse(bg, (255, 0, 0), [400, 160, 60, 35], 5)
#     pygame.draw.line(bg, (255, 0, 255), (280, 220), (320, 220), 3)




######################匯入模組######################
import pygame
import sys
######################初始化#######################
pygame.init() # 啟動 Pygame
width = 640 # 設定視窗寬度
height = 320 # 設定視窗高度
##################建立視窗及物件##################### 設定視窗大小
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
         # 繪製畫布於視窗左上角
    screen.blit(bg, (0, 0))
    # 更新視窗
    pygame.display.update()
######################繪製圖形######################
# 畫圓形, (畫布, 顏色, 圓心, 半徑, 線寬)
    pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)
    pygame.draw.circle(bg, (0, 0, 255), (200, 100), 30, 0)