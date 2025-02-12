# 벽돌깨기 게임
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = 800
pygame.init()
Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Paygame Blocks!!')
pygame.key.set_repeat(10, 10)

def main():
    is_game_star = False
    score = 0
    BLOCK = []
    # 클래스 생성
    # 무지개색 정보
    colors = [(255, 0, 0), (255, 150, 0), (255, 228, 0), (11, 201, 4),
              (0, 80, 255), (0, 0, 147), (201, 0, 167)]

    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('Game START?', True, 'white')
    M_GAME_SUBTITLE = bigFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('GAME START?', True, 'yellow')
    M_FAIL = bigFont.render('FAILED', True, 'red')

    while True:
        Surface.fill(color='black') # Surface.fill((0, 0, 0))
        for event in pygame.event.get(): # 이벤트 처리
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                pass
                if event.key == K_LEFT:
                    pass
                elif event.key == K_RIGHT:
                    pass
                elif event.key == K_SPACE:
                    is_game_star = True # 게임시작

        # 게임화면 렌더링
        if is_game_star == False:
            Surface.blit(M_GAME_TITLE, ((SCREEN_WIDTH / 2) - (400 / 2), 
                                        (SCREEN_HEIGTH / 2) - (50 / 2)))
            Surface.blit(M_GAME_SUBTITLE, ((SCREEN_WIDTH / 2) - (300 / 2),
                                           (SCREEN_HEIGTH / 2) + 50))
        else: # 게임 시작 후 블록 다 그리고 볼이 움직이게 처리, 바도 움직이도록 
            Surface.blit(M_CLEAR, (80, 280))

        pygame.display.update() 
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()