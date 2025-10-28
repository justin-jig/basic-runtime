# 48_pygame_galaga_collision_effects.py
import pygame
import random
from time import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW= (255, 230, 64)
pad_w, pad_h = 480, 640
fw, fh = 36, 38
ew, eh = 26, 20

def safe_img(path, size, color):
    try:
        return pygame.image.load(path)
    except Exception:
        s = pygame.Surface(size, pygame.SRCALPHA)
        s.fill(color)
        return s

class PopupText:
    def __init__(self, txt, x, y, color=YELLOW, ttl=0.6):
        self.txt, self.x, self.y = txt, x, y
        self.color, self.ttl = color, ttl
        self.birth = time()
        self.font = pygame.font.SysFont(None, 24)
    def draw(self, screen):
        elapsed = time() - self.birth
        if elapsed > self.ttl: return False
        alpha = max(0, 255 - int(255 * (elapsed / self.ttl)))
        surf = self.font.render(self.txt, True, self.color)
        surf.set_alpha(alpha)
        screen.blit(surf, (self.x, self.y - int(elapsed * 40)))
        return True

class Explosion:
    def __init__(self, x, y, sprite=None):
        self.x, self.y = x, y
        self.sprite = sprite  # 스프라이트(옵션)
        self.birth = time()
        self.duration = 0.4
        self.max_r = 24
    def draw(self, screen):
        t = time() - self.birth
        if t > self.duration: return False
        if self.sprite:
            # 간단히 알파 페이드
            s = self.sprite.copy()
            alpha = max(0, 255 - int(255 * (t / self.duration)))
            s.set_alpha(alpha)
            rect = s.get_rect(center=(self.x, self.y))
            screen.blit(s, rect)
        else:
            # 원형 확장
            r = int((t / self.duration) * self.max_r) + 4
            s = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 160, 0, 180), (r, r), r)
            pygame.draw.circle(s, (255, 255, 255, 120), (r, r), max(1, r//2))
            screen.blit(s, (self.x - r, self.y - r))
        return True

def flash(screen, alpha=120):
    overlay = pygame.Surface((pad_w, pad_h))
    overlay.fill((255, 255, 255))
    overlay.set_alpha(alpha)
    screen.blit(overlay, (0, 0))

def run():
    pygame.init()
    screen = pygame.display.set_mode((pad_w, pad_h))
    pygame.display.set_caption("Galaga + Collision Effects")
    clock = pygame.time.Clock()

    fighter = safe_img("fighter.png", (fw, fh), (80, 160, 240))
    enemy   = safe_img("enemy.png", (ew, eh), (240, 80, 80))
    bullet  = safe_img("bullet.png", (4, 10), (255, 255, 0))
    explosion_sprite = safe_img("explosion.png", (32, 32), (255, 0, 0))  # 없으면 원형 이펙트

    x, y, dx = pad_w * 0.45, pad_h * 0.9, 0
    bullets, exps, pops = [], [], []
    ex_flash = 0  # 플래시 남은 프레임 수

    enemy_x = random.randrange(0, pad_w - ew)
    enemy_y = 0
    enemy_speed = 3
    kills, passed = 0, 0

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:  dx = -5
                if e.key == pygame.K_RIGHT: dx =  5
                if e.key == pygame.K_LCTRL and len(bullets) < 2:
                    bullets.append([x + fw/2, y - fh])
            elif e.type == pygame.KEYUP:
                if e.key in (pygame.K_LEFT, pygame.K_RIGHT): dx = 0

        # 업데이트
        x = max(0, min(pad_w - fw, x + dx))

        # 전투기 vs 적 충돌
        if y < enemy_y + eh:
            if (enemy_x > x and enemy_x < x + fw) or (enemy_x + ew > x and enemy_x + ew < x + fw):
                running = False

        # 탄 이동/충돌
        i = 0
        while i < len(bullets):
            bullets[i][1] -= 10
            bx, by = bullets[i]
            if by < enemy_y and enemy_x <= bx <= enemy_x + ew:
                del bullets[i]
                kills += 1
                enemy_speed = min(enemy_speed + 1, 10)
                # 효과 추가
                exps.append(Explosion(enemy_x + ew//2, enemy_y + eh//2, explosion_sprite))
                pops.append(PopupText("+100", enemy_x + ew//2, enemy_y))
                ex_flash = 6  # 짧은 화면 플래시
                # 적 리셋
                enemy_x = random.randrange(0, pad_w - ew)
                enemy_y = 0
                continue
            if by <= 0:
                del bullets[i]; continue
            i += 1

        # 적 이동
        enemy_y += enemy_speed
        if enemy_y > pad_h:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_w - ew)
            passed += 1
            if passed >= 3: running = False

        # 렌더
        screen.fill(BLACK)
        screen.blit(fighter, (x, y))
        screen.blit(enemy, (enemy_x, enemy_y))
        for bx, by in bullets:
            screen.blit(bullet, (bx, by))

        # 이펙트 그리기(살아있는 것만 유지)
        exps[:] = [e for e in exps if e.draw(screen)]
        pops[:] = [p for p in pops if p.draw(screen)]

        # 화면 플래시
        if ex_flash > 0:
            flash(screen, 120)
            ex_flash -= 1

        # UI
        font = pygame.font.SysFont(None, 20)
        screen.blit(font.render(f"Kills: {kills}", True, WHITE), (8, 8))
        screen.blit(font.render(f"Passed: {passed}", True, WHITE), (pad_w - 120, 8))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run()
