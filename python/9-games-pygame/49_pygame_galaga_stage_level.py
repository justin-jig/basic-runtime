# 49_pygame_galaga_stage_level.py
import pygame
import random

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,80,80)
GREEN=(80,220,120)

W,H = 480,640
FW,FH = 36,38
EW,EH = 26,20

def safe_img(path,size,color):
    try: return pygame.image.load(path)
    except: 
        s = pygame.Surface(size, pygame.SRCALPHA); s.fill(color); return s

def draw_text(screen, s, pos, color=WHITE, size=20, center=False):
    font = pygame.font.SysFont(None, size)
    surf = font.render(s, True, color)
    rect = surf.get_rect()
    rect.topleft = pos
    if center:
        rect.center = pos
    screen.blit(surf, rect)

class Enemy:
    def __init__(self, x, y, speed):
        self.x, self.y, self.speed = x, y, speed
    def update(self):
        self.y += self.speed
    def rect(self): return pygame.Rect(self.x, self.y, EW, EH)

class Boss:
    def __init__(self, hp, speed):
        self.w, self.h = 72, 40
        self.x = (W - self.w)//2
        self.y = 50
        self.hp_max = hp
        self.hp = hp
        self.speed = speed
        self.dir = 1
    def update(self):
        self.x += self.dir * self.speed
        if self.x < 0 or self.x > W - self.w:
            self.dir *= -1
    def hit(self, dmg=1):
        self.hp = max(0, self.hp - dmg)
        return self.hp == 0
    def rect(self): return pygame.Rect(self.x, self.y, self.w, self.h)
    def draw_bar(self, screen):
        # 보스 HP 바
        bw, bh = 200, 10
        bx, by = (W - bw)//2, 16
        pygame.draw.rect(screen, RED, (bx, by, bw, bh))
        rw = int(bw * (self.hp / self.hp_max))
        pygame.draw.rect(screen, GREEN, (bx, by, rw, bh))
        draw_text(screen, "BOSS", (bx - 50, by - 2))

def run():
    pygame.init()
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Galaga + Stage/Level")
    clock = pygame.time.Clock()

    fighter = safe_img("fighter.png", (FW,FH), (80,160,240))
    enemy_img = safe_img("enemy.png", (EW,EH), (240,80,80))
    bullet   = safe_img("bullet.png", (4,10), (255,255,0))
    boss_img = safe_img("boss.png", (72,40), (240,120,0))

    x, y, dx = W*0.45, H*0.9, 0
    bullets = []
    enemies = []
    boss = None

    level = 1
    kills = 0
    passed = 0
    spawn_cd = 0
    KILL_TO_LEVELUP = 5  # 5킬마다 레벨업
    base_speed = 2

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: running=False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:  dx=-5
                if e.key == pygame.K_RIGHT: dx= 5
                if e.key == pygame.K_LCTRL and len(bullets) < 3:
                    bullets.append([x+FW/2, y-FH])
            elif e.type == pygame.KEYUP:
                if e.key in (pygame.K_LEFT, pygame.K_RIGHT): dx=0

        # 레벨 → 난이도 스케일
        speed_scale = base_speed + (level-1)*0.6

        # 스폰(보스 없는 경우만 일반 적 스폰)
        if boss is None:
            spawn_cd -= 1
            if spawn_cd <= 0 and len(enemies) < 6:
                ex = random.randrange(0, W-EW)
                enemies.append(Enemy(ex, 0, random.uniform(1.5, 2.5)+speed_scale*0.2))
                spawn_cd = max(10, 30 - level*2)

        # 이동
        x = max(0, min(W-FW, x+dx))
        for en in enemies: en.update()
        if boss: 
            boss.update()

        # 충돌(전투기 vs 적/보스)
        p_rect = pygame.Rect(x, y, FW, FH)
        if boss and p_rect.colliderect(boss.rect()):
            running=False
        i=0
        while i < len(enemies):
            if enemies[i].rect().colliderect(p_rect):
                running=False; break
            if enemies[i].y > H:
                passed += 1
                del enemies[i]
                continue
            i+=1

        # 총알 이동 & 타격
        bi=0
        while bi < len(bullets):
            bullets[bi][1] -= 10
            bx, by = bullets[bi]
            brect = pygame.Rect(bx, by, 4, 10)

            hit_any = False

            # 보스 우선 체크
            if boss and brect.colliderect(boss.rect()):
                del bullets[bi]; hit_any=True
                if boss.hit(1):
                    boss = None
                    kills += 5  # 보스 처치 보너스
                # 보스 처치/타격시 별도 처리 가능
            if hit_any:
                continue

            # 일반 적
            j=0
            while j < len(enemies) and not hit_any:
                if brect.colliderect(enemies[j].rect()):
                    del bullets[bi]
                    del enemies[j]
                    kills += 1
                    hit_any=True
                    break
                j+=1
            if hit_any:
                continue

            # 화면 밖
            if by <= 0:
                del bullets[bi]; continue
            bi+=1

        # 레벨업 & 보스 소환 로직
        if boss is None and kills > 0 and kills % KILL_TO_LEVELUP == 0:
            # 레벨업 순간에만 보스 소환 (중복 방지)
            if not any(isinstance(en, Boss) for en in enemies):
                level += 1
                enemies.clear()
                boss = Boss(hp=8 + level*2, speed=2 + level*0.3)

        # 렌더
        screen.fill(BLACK)
        screen.blit(fighter, (x,y))

        for en in enemies:
            screen.blit(enemy_img, (en.x, en.y))

        if boss:
            screen.blit(boss_img, (boss.x, boss.y))
            boss.draw_bar(screen)

        for bx, by in bullets:
            screen.blit(bullet, (bx, by))

        draw_text(screen, f"LV {level}", (8,8))
        draw_text(screen, f"Kills: {kills}", (8,30))
        draw_text(screen, f"Passed: {passed}", (W-130,8))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run()
