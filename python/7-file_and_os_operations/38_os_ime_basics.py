# 38_os_and_time_basics.py
# OS 디렉터리 관리, 파일 구분, 로그 작성, 날짜/시간 계산 예제 모음

# ------------------------------------------------------------
# 1) 현재 디렉터리 확인 및 이동
# ------------------------------------------------------------
import os

pdir = os.getcwd()          # 현재 작업 디렉터리
print('[현재 디렉터리]', pdir)

os.chdir('..')              # 상위 디렉터리로 이동
print('[상위 디렉터리]', os.getcwd())

os.chdir(pdir)              # 다시 원래 디렉터리로 이동
print('[복귀 디렉터리]', os.getcwd())

# ------------------------------------------------------------
# 2) 디렉터리 생성 (mkdir)
# ------------------------------------------------------------
newfolder = input('\n새로 생성할 디렉터리 이름을 입력하세요: ')
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리를 새로 생성했습니다.' % newfolder)
except Exception as e:
    print(e)

# ------------------------------------------------------------
# 3) 디렉터리 삭제 (rmdir)
# ------------------------------------------------------------
target_folder = 'tmp'
k = input('\n[%s] 디렉터리를 삭제하겠습니까? (y/n) ' % target_folder)
if k.lower() == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제했습니다.' % target_folder)
    except Exception as e:
        print(e)

# ------------------------------------------------------------
# 4) 하위 폴더 및 파일 전체 삭제 (shutil.rmtree)
# ------------------------------------------------------------
import shutil

target_folder = 'd:/devlab/py200/tmp'
print('\n[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.' % target_folder)
for file in os.listdir(target_folder):
    print(file)

k = input('[%s]를 삭제하겠습니까? (y/n) ' % target_folder)
if k.lower() == 'y':
    try:
        shutil.rmtree(target_folder)
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다.' % target_folder)
    except Exception as e:
        print(e)

# ------------------------------------------------------------
# 5) 디렉터리 존재 여부 확인 (exists)
# ------------------------------------------------------------
from os.path import exists

dir_name = input('\n새로 생성할 디렉터리 이름을 입력하세요: ')
if not exists(dir_name):
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성했습니다.' % dir_name)
else:
    print('[%s]은(는) 이미 존재합니다.' % dir_name)

# ------------------------------------------------------------
# 6) 파일 / 디렉터리 구분 출력
# ------------------------------------------------------------
from os.path import isdir, isfile

print('\n현재 디렉터리 내 항목 구분:')
files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR : %s' % file)
for file in files:
    if isfile(file):
        print('FILE: %s' % file)

# ------------------------------------------------------------
# 7) 로그 파일에 시간 정보 기록
# ------------------------------------------------------------
from time import localtime, strftime

logfile = 'test.log'

def writelog(logfile, log):
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'
    with open(logfile, 'a', encoding='utf-8') as f:
        f.writelines(log)

writelog(logfile, '2번째 로깅 문장입니다.')
print('\n[test.log]에 로그가 기록되었습니다.')

# ------------------------------------------------------------
# 8) 오늘 날짜 기준 경과 일수 계산
# ------------------------------------------------------------
from time import localtime

t = localtime()
start_day = '%d-01-01' % t.tm_year
elapsed_day = t.tm_yday
print('\n오늘은 [%s] 이후 [%d]일째 되는 날입니다.' % (start_day, elapsed_day))

# ------------------------------------------------------------
# 9) 요일 계산
# ------------------------------------------------------------
weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

t = localtime()
today = '%d-%d-%d' % (t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday]
print('[%s] 오늘은 [%s]입니다.' % (today, week))

# ------------------------------------------------------------
# 10) datetime으로 수행 시간 측정
# ------------------------------------------------------------
from datetime import datetime

start = datetime.now()
print('\n1에서 백만까지 더합니다...')
ret = 0
for i in range(1_000_000):
    ret += i
print('1에서 백만까지 더한 결과: %d' % ret)

end = datetime.now()
elapsed = end - start
print('총 계산 시간: ', end=''); print(elapsed)
elapsed_ms = int(elapsed.total_seconds() * 1000)
print('총 계산 시간: %dms' % elapsed_ms)
