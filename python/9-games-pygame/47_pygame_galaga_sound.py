# 47_pygame_galaga_sound.py
import pygame
import random
from time import sleep

# 색/크기
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pad_width, pad_height = 480, 640
fight_w, fight_h = 36, 38
enemy_w, enemy_h = 26, 20

# 사운드 핸들(없으면 None)
bgm = fire_snd = boom_snd = None

def safe_load_image(path, size, color):
    try:
        img = pygame.image.load(path)
    except Exception:
        img = pygame.Surface(size)
        img.fill(color)
    return img

def try_init_sound():
    global bgm, fire_snd, boom_snd
    try:
        pygame.mixer.init()
        # 파일이 있으면 사용, 없으면 로드 실패 → 예외 처리
        try:
            bgm = pygame.mixer.Sound("bgm.ogg")
            bgm.set_volume(0.3)
            bgm.play(-1)  # 루프
        except Exception:
            bgm = None
        try:
            fire_snd = pygame.mixer.Sound("fire.wav")
        except Exception:
            fire_snd = None
        try:
            boom_snd = pygame.mixer.Sound("boom.wav")
        except Exception:
            boom_snd = None
    except Exception:
        bgm = fire_snd = boom_snd = None

def play_fire():
    if fire_snd:
        fire_snd.play()

def play_boom():
    if boom_snd:
        boom_snd.play()

def draw(screen, obj, x, y):
    screen.blit(obj, (x, y))

def text(screen, s, pos, color=WHITE, size=20):
    font = pygame.font.SysFont(None, size)
    screen.blit(font.render(s, True, color), pos)

def run():
    pygame.init()
    screen = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.setCaption = pygame.display.set_caption
    pygame.display.setCaption("Galaga + Sound")
    clock = pygame.time.Clock()

    try_init_sound()

    fighter = safe_load_image("fighter.png", (fight_w, fight_h), (80, 160, 240))
    enemy   = safe_load_image("enemy.png", (enemy_w, enemy_h), (240, 80, 80))
    bullet  = safe_load_image("bullet.png", (4, 10), (255, 255, 0))

    # 상태
    x = pad_width * 0.45
    y = pad_height * 0.9
    dx = 0
    bullets = []           # [x, y]
    enemy_x = random.randrange(0, pad_width - enemy_w)
    enemy_y = 0
    enemy_speed = 3
    kills = passed = 0

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:  dx = -5
                if e.key == pygame.K_RIGHT: dx =  5
                if e.key == pygame.K_LCTRL and len(bullets) < 2:
                    bullets.append([x + fight_w / 2, y - fight_h])
                    play_fire()
            elif e.type == pygame.KEYUP:
                if e.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    dx = 0

        # 업데이트
        x = max(0, min(pad_width - fight_w, x + dx))

        # 충돌(전투기 vs 적)
        if y < enemy_y + enemy_h:
            if (enemy_x > x and enemy_x < x + fight_w) or (enemy_x + enemy_w > x and enemy_x + enemy_w < x + fight_w):
                play_boom()
                sleep(0.5)
                running = False

        # 탄 이동/충돌
        i = 0
        while i < len(bullets):
            bullets[i][1] -= 10
            bx, by = bullets[i]
            if by < enemy_y and enemy_x <= bx <= enemy_x + enemy_w:
                play_boom()
                del bullets[i]
                kills += 1
                enemy_speed = min(enemy_speed + 1, 10)
                enemy_x = random.randrange(0, pad_width - enemy_w)
                enemy_y = 0
                continue
            if by <= 0:
                del bullets[i]
                continue
            i += 1

        # 적 이동
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_w)
            passed += 1
            if passed >= 3:
                running = False

        # 렌더
        screen.fill(BLACK)
        draw(screen, fighter, x, y)
        draw(screen, enemy, enemy_x, enemy_y)
        for bx, by in bullets:
            draw(screen, bullet, bx, by)

        text(screen, f"Kills: {kills}", (8, 8))
        text(screen, f"Passed: {passed}", (pad_width - 120, 8))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run()
