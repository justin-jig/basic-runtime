# 45_pygame_galaga_progressive.py
# Pygame Galaga 실습(3단계):
#  1단계: 빈 화면 갱신
#  2단계: 전투기 이동 (좌/우)
#  3단계: 적 등장 및 하강

import pygame
import random

BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 38
enemy_width = 26
enemy_height = 20

def placeholder_surface(w, h, color=(200, 200, 200)):
    """이미지 파일이 없을 때 대체 Surface 생성"""
    surf = pygame.Surface((w, h))
    surf.fill(color)
    return surf

def drawObject(screen, obj, x, y):
    screen.blit(obj, (x, y))

def stage1_loop(screen, clock):
    """1단계: 빈 화면(검정) 갱신"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        pygame.display.update()
        clock.tick(60)

def stage2_loop(screen, clock, fighter):
    """2단계: 좌우 이동"""
    x = pad_width * 0.45
    y = pad_height * 0.9
    x_change = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        screen.fill(BLACK)
        x += x_change
        x = max(0, min(x, pad_width - fighter_width))
        drawObject(screen, fighter, x, y)
        pygame.display.update()
        clock.tick(60)

def stage3_loop(screen, clock, fighter, enemy):
    """3단계: 적 등장 및 하강"""
    x = pad_width * 0.45
    y = pad_height * 0.9
    x_change = 0

    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        screen.fill(BLACK)

        # 전투기 이동
        x += x_change
        x = max(0, min(x, pad_width - fighter_width))
        drawObject(screen, fighter, x, y)

        # 적 하강
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
        drawObject(screen, enemy, enemy_x, enemy_y)

        pygame.display.update()
        clock.tick(60)

def run(stage=1):
    pygame.init()
    screen = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    clock = pygame.time.Clock()

    # 리소스 로드 (없으면 placeholder 사용)
    try:
        fighter = pygame.image.load('fighter.png')
    except Exception:
        fighter = placeholder_surface(fighter_width, fighter_height, (80, 160, 240))
    try:
        enemy = pygame.image.load('enemy.png')
    except Exception:
        enemy = placeholder_surface(enemy_width, enemy_height, (240, 80, 80))

    if stage == 1:
        stage1_loop(screen, clock)
    elif stage == 2:
        stage2_loop(screen, clock, fighter)
    else:
        stage3_loop(screen, clock, fighter, enemy)

    pygame.quit()

if __name__ == '__main__':
    # 원하는 단계로 실행: 1(빈화면), 2(이동), 3(적 등장)
    run(stage=3)
