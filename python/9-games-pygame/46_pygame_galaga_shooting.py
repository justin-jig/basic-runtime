import pygame
import random
from time import sleep

# 색/크기
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

pad_width = 480
pad_height = 640
fight_width = 36
fight_height = 38
enemy_width = 26
enemy_height = 20

def drawObject(obj, x, y):
    gamepad.blit(obj, (x, y))

def dispMessage(text):
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    surf = textfont.render(text, True, RED)
    rect = surf.get_rect()
    rect.center = (pad_width / 2, pad_height / 2)
    gamepad.blit(surf, rect)
    pygame.display.update()
    sleep(2)

def gameover():
    dispMessage('Game Over')
    runGame()  # 재시작

def crash():
    dispMessage('Crashed!')
    runGame()  # 재시작

def drawScore(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Kills: ' + str(count), True, WHITE)
    gamepad.blit(text, (0, 0))

def drawPassed(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Passed: ' + str(count), True, RED)
    gamepad.blit(text, (360, 0))

def runGame():
    global gamepad, fighter, clock, bullet, enemy

    isShot = False
    shotcount = 0
    enemypassed = 0

    # 전투기
    x = pad_width * 0.45
    y = pad_height * 0.9
    x_change = 0

    # 총알
    bullet_xy = []  # [x, y] 목록 (최대 2발)

    # 적
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
                elif event.key == pygame.K_LCTRL:
                    if len(bullet_xy) < 2:
                        bullet_x = x + fight_width / 2
                        bullet_y = y - fight_height
                        bullet_xy.append([bullet_x, bullet_y])

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0

        gamepad.fill(BLACK)

        # 전투기 이동/경계
        x += x_change
        x = max(0, min(x, pad_width - fight_width))

        # 충돌(전투기 vs 적)
        if y < enemy_y + enemy_height:
            if (enemy_x > x and enemy_x < x + fight_width) or \
               (enemy_x + enemy_width > x and enemy_x + enemy_width < x + fight_width):
                crash()

        drawObject(fighter, x, y)

        # 총알 이동/충돌/삭제
        i = 0
        while i < len(bullet_xy):
            bullet_xy[i][1] -= 10
            bx, by = bullet_xy[i]
            # 적과 y축 상단에서 만나는 단순 충돌
            if by < enemy_y and enemy_x <= bx <= enemy_x + enemy_width:
                del bullet_xy[i]
                isShot = True
                shotcount += 1
                continue
            if by <= 0:
                del bullet_xy[i]
                continue
            i += 1

        for bx, by in bullet_xy:
            drawObject(bullet, bx, by)

        drawScore(shotcount)

        # 적 이동/리셋
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemy_y = 0
            enemypassed += 1

        if enemypassed == 3:
            gameover()

        drawPassed(enemypassed)

        if isShot:
            enemy_speed = min(enemy_speed + 1, 10)
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemy_y = 0
            isShot = False

        drawObject(enemy, enemy_x, enemy_y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, fighter, clock, bullet, enemy

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')

    try:
        fighter = pygame.image.load('fighter.png')
    except Exception:
        fighter = pygame.Surface((fight_width, fight_height)); fighter.fill((80, 160, 240))

    try:
        enemy = pygame.image.load('enemy.png')
    except Exception:
        enemy = pygame.Surface((enemy_width, enemy_height)); enemy.fill((240, 80, 80))

    try:
        bullet = pygame.image.load('bullet.png')
    except Exception:
        bullet = pygame.Surface((4, 10)); bullet.fill((255, 255, 0))

    clock = pygame.time.Clock()

if __name__ == '__main__':
    initGame()
    runGame()
