# 37_file_io_basics.py
# 파일 읽기/쓰기 기본 + 심화: writelines, 텍스트/바이너리 복사, with open, seek/부분 복사,
# 파일 크기, 삭제/이름변경/이동, 디렉터리 목록/글롭 패턴

# ─────────────────────────────────────────────────────────────
# 0) (기본) 텍스트 전체 읽기 / 한 줄씩 읽기 / 여러 줄 읽기 / 쓰기
# ─────────────────────────────────────────────────────────────

# 전체 읽기 (read)
f = open('stockcode.txt', 'r', encoding='utf-8')
data = f.read()
print('[전체 읽기 결과]')
print(data)
f.close()

# 한 줄씩 읽기 (readline)
f = open('stockcode.txt', 'r', encoding='utf-8')
line_num = 1
line = f.readline()
while line:
    print('%d %s' % (line_num, line), end='')
    line = f.readline()
    line_num += 1
f.close()

# 여러 줄 읽기 (readlines)
f = open('stockcode.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line_num, line in enumerate(lines, start=1):
    print('%d %s' % (line_num, line), end='')
f.close()

# 쓰기 (write)
text = input('\n파일에 저장할 내용을 입력하세요: ')
f = open('mydata.txt', 'w', encoding='utf-8')
f.write(text)
f.close()

# 저장 확인
h = open('mydata.txt', 'r', encoding='utf-8')
text = h.read()
print('\n[파일 저장 확인]')
print(text)
h.close()

# ─────────────────────────────────────────────────────────────
# 1) (심화) 여러 줄 입력 → writelines 로 저장
# ─────────────────────────────────────────────────────────────
count = 1
data = []
print('\n파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
while True:
    text = input('[%d] 파일에 저장할 내용을 입력하세요: ' % count)
    if text == '':
        break
    data.append(text + '\n')
    count += 1

f = open('mydata.txt', 'w', encoding='utf-8')
f.writelines(data)
f.close()

# ─────────────────────────────────────────────────────────────
# 2) 텍스트 파일 복사 (read → write)
# ─────────────────────────────────────────────────────────────
f = open('stockcode.txt', 'r', encoding='utf-8')
h = open('stockcode_copy.txt', 'w', encoding='utf-8')
data = f.read()
h.write(data)
f.close()
h.close()
print('[텍스트 복사] stockcode.txt -> stockcode_copy.txt 완료')

# ─────────────────────────────────────────────────────────────
# 3) 바이너리 파일 복사 (버퍼 단위)
# ─────────────────────────────────────────────────────────────
bufsize = 1024
f = open('img_sample.jpg', 'rb')
h = open('img_sample_copy.jpg', 'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()
print('[바이너리 복사] img_sample.jpg -> img_sample_copy.jpg 완료')

# ─────────────────────────────────────────────────────────────
# 4) with open + enumerate (권장 패턴)
# ─────────────────────────────────────────────────────────────
print('\n[with open + enumerate]')
with open('stockcode.txt', 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f.readlines(), start=1):
        print('%d %s' % (line_num, line), end='')

# ─────────────────────────────────────────────────────────────
# 5) seek/부분 읽기 → 부분 파일로 저장
# ─────────────────────────────────────────────────────────────
spos = 105    # 시작 위치
size = 500    # 읽을 크기

f = open('stockcode.txt', 'r', encoding='utf-8')
h = open('stockcode_part.txt', 'w', encoding='utf-8')
f.seek(spos)
data = f.read(size)
h.write(data)
h.close()
f.close()
print('\n[부분 복사] stockcode_part.txt 생성 (offset=%d, size=%d)' % (spos, size))

# ─────────────────────────────────────────────────────────────
# 6) 파일 크기 확인 (os.path.getsize)
# ─────────────────────────────────────────────────────────────
from os.path import getsize

file1 = 'stockcode.txt'
file2 = 'd:/devlab/py200/img_sample.jpg'  # 플랫폼/환경에 따라 존재하지 않을 수 있음

try:
    file_size1 = getsize(file1)
    print('File Name: %s \tFile Size: %d' % (file1, file_size1))
except FileNotFoundError:
    print('경고: %s 파일이 존재하지 않습니다.' % file1)

try:
    file_size2 = getsize(file2)
    print('File Name: %s \tFile Size: %d' % (file2, file_size2))
except FileNotFoundError:
    print('경고: %s 파일이 존재하지 않습니다.' % file2)

# ─────────────────────────────────────────────────────────────
# 7) 파일 삭제 (os.remove)
# ─────────────────────────────────────────────────────────────
from os import remove

target_file = 'stockcode_copy.txt'
k = input('\n[%s] 파일을 삭제하겠습니까? (y/n) ' % target_file).strip().lower()
if k == 'y':
    try:
        remove(target_file)
        print('[%s]를 삭제했습니다.' % target_file)
    except FileNotFoundError:
        print('이미 삭제되었거나 존재하지 않습니다: %s' % target_file)

# ─────────────────────────────────────────────────────────────
# 8) 파일 이름 변경 (os.rename)
#    주의: 이름을 변경하면 이후 코드에서 기존 파일명이 없을 수 있음
# ─────────────────────────────────────────────────────────────
from os import rename

target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일 이름을 입력하세요: ' % target_file).strip()

if newname:
    try:
        rename(target_file, newname)
        print('[%s] -> [%s] 로 파일이름이 변경되었습니다.' % (target_file, newname))
        # 이후 실습을 위해 다시 원래 이름으로 되돌릴지 여부 선택
        revert = input('원래 이름(%s)으로 되돌릴까요? (y/n) ' % target_file).strip().lower()
        if revert == 'y':
            rename(newname, target_file)
            print('[%s] -> [%s] 로 되돌렸습니다.' % (newname, target_file))
        else:
            # 이후 예제에서 사용할 이름을 갱신
            target_file = newname
    except FileNotFoundError as e:
        print(e)

# ─────────────────────────────────────────────────────────────
# 9) 파일 이동 (rename로 경로 변경)
# ─────────────────────────────────────────────────────────────
from os import rename as mv_rename

target_file = 'stockcode.txt'  # 위에서 이름을 바꿨다면 존재하지 않을 수 있음
newpath = input('[%s]를 이동할 디렉터리의 절대경로를 입력하세요: ' % target_file).strip()

if newpath:
    if newpath[-1] == '/' or newpath.endswith('\\'):
        newfull = newpath + target_file
    else:
        # OS에 따라 구분자 상이: 간단히 '/' 사용 (Windows도 허용되는 경우 많음)
        newfull = newpath + '/' + target_file
    try:
        mv_rename(target_file, newfull)
        print('[%s] -> [%s] 로 이동되었습니다.' % (target_file, newfull))
    except FileNotFoundError as e:
        print('이동 실패:', e)

# ─────────────────────────────────────────────────────────────
# 10) 디렉터리 목록 / 글롭 패턴
# ─────────────────────────────────────────────────────────────
import os, glob

folder = 'd:/devlab/py200'  # 환경에 따라 없을 수 있음
try:
    file_list = os.listdir(folder)
    print('\n[%s] 목록:' % folder, file_list)
except FileNotFoundError:
    print('\n경고: 목록을 조회할 수 없습니다. 폴더가 존재하지 않습니다 ->', folder)

files = '*.txt'
file_list = glob.glob(files)
print('[글롭] 현재 폴더의 %s 목록:' % files, file_list)


# ─────────────────────────────────────────────────────────────
# 11) 텍스트 파일 분석: 문자 빈도수(top-down) & 단어수
# ─────────────────────────────────────────────────────────────
def getTextFreq(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        fa = {}
        for c in text:
            fa[c] = fa.get(c, 0) + 1
    return fa

freq = getTextFreq('mydata.txt')
freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print('\n[문자 빈도수]')
for c, n in freq_sorted:
    if c == '\n':
        continue
    print('[%c] -> [%d]회 나타남' % (c, n))

with open('mydata.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    words = data.split()
    print('단어수: [%d]' % len(words))

# ─────────────────────────────────────────────────────────────
# 12) 특정 단어 개수 세기 (대소문자 무시)
# ─────────────────────────────────────────────────────────────
def countWord(filename, word):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    word = word.lower()
    pos, count = text.find(word), 0
    while pos != -1:
        count += 1
        pos = text.find(word, pos + 1)
    return count

word = input('\nmydata.txt에서 개수를 구할 단어를 입력하세요: ').strip()
wc = countWord('mydata.txt', word)
print('[%s]의 개수: %d' % (word, wc))

# ─────────────────────────────────────────────────────────────
# 13) 파일 내 단어 치환 후 새 파일로 저장
# ─────────────────────────────────────────────────────────────
t1 = input('찾을 단어를 입력하세요: ')
t2 = input('변경할 단어를 입력하세요: ')
with open('mydata.txt', 'r', encoding='utf-8') as f, \
     open('mydata2.txt', 'w', encoding='utf-8') as h:
    text = f.read()
    text = text.replace(t1, t2)
    h.write(text)
print('[%s]를 [%s]로 변경하였습니다. → mydata2.txt' % (t1, t2))
