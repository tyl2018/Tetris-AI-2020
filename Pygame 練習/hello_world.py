# 載入相關資料庫
# 使用Pygame前需要先install
# https://www.pygame.org/wiki/GettingStarted
import pygame, sys
from pygame.locals import *

pygame.init() # 初始化
DISPLAYSURF = pygame.display.set_mode((400, 300))  # 設定視窗大小
pygame.display.set_caption('Hello Tetris :D')     # 設定視窗標題
while True: # 主迴圈
    for event in pygame.event.get(): # pygame.event.get() 會回傳一個list，包含目前所有event. 將其中的每一項令為event並執行for loop內的內容
        if event.type == QUIT: # 此event為「視窗被按x」的時候
            # 關掉視窗
            pygame.quit()
            sys.exit()  # 這行如果是用Jupyter執行會卡，要用exit()取代
        pygame.display.update()
