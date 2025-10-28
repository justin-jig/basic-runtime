# 42_random_practice.py
# 로또 번호 생성 & 랜덤 커플 매칭

from random import shuffle
from time import sleep

# ------------------------------------------------------------
# 1) 로또 번호 생성 (회수 입력받아 반복)
# ------------------------------------------------------------
gamenum = input('로또 게임 회수를 입력하세요: ')
try:
    gamenum = int(gamenum)
except ValueError:
    gamenum = 1

for i in range(gamenum):
    balls = [x + 1 for x in range(45)]
    ret = []
    for _ in range(6):
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    print('로또번호[%d]: ' % (i + 1), ret)
    sleep(1)

# ------------------------------------------------------------
# 2) 랜덤 커플 매칭 (zip)
# ------------------------------------------------------------
male = ['슈퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우먼', '뺑덕', '줄리엣', '성춘향', '아라치']
shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, (m, f) in enumerate(couples, start=1):
    print('커플%d: [%s]-[%s]' % (i, m, f))
