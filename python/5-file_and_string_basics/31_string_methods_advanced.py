# 31_string_methods_advanced.py
# 문자열 고급 메서드, 분리/결합, 치환, 인코딩/디코딩, 정렬 예제 모음

# ------------------------------------------------------------
# 1) 문자열 내 특정 문자/단어 개수 세기 (count)
# ------------------------------------------------------------
txt = 'A lot of things occur each day, every day.'
word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count(' ')
print('[count] 결과:', word_count1, word_count2, word_count3)

# ------------------------------------------------------------
# 2) 문자열 내 특정 단어 위치 찾기 (find)
# ------------------------------------------------------------
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print('\n[find] 결과:', offset1, offset2, offset3)

# ------------------------------------------------------------
# 3) 문자열 분리 (split)
# ------------------------------------------------------------
url = 'http://www.naver.com/news/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/')
print('\n[split] URL 분리:', ret1)

ret2 = log.split()
print('[split] 로그 항목:')
for data in ret2:
    d1, d2 = data.split(':')
    print(f'{d1} -> {d2}')

# ------------------------------------------------------------
# 4) 문자열 결합 (join)
# ------------------------------------------------------------
loglist = ['2016/08/26 10:12:11', '200', 'OK', '이 또한 지나가리라']
bond = ';'
log = bond.join(loglist)
print('\n[join] 결합 결과:', log)

# ------------------------------------------------------------
# 5) 문자열 치환 (replace)
# ------------------------------------------------------------
txt = 'My password is 1234'
ret1 = txt.replace('1', '0')
ret2 = txt.replace('1', 'python')
print('\n[replace] 숫자 치환:')
print(ret1)
print(ret2)

txt = '매일 많은 일들이 일어납니다.'
ret3 = txt.replace('매일', '항상')
ret4 = ret3.replace('일', '사건')
print('[replace] 한글 문자열 치환:')
print(ret3)
print(ret4)

# ------------------------------------------------------------
# 6) 인코딩 / 디코딩
# ------------------------------------------------------------
u_txt = 'I love python'
b_txt = u_txt.encode()  # str → bytes
print('\n[encode/decode]')
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]  # byte 비교
print(ret1, ret2)

b_txt = b'A lot of things occur each day.'
u_txt = b_txt.decode()  # bytes → str
print(u_txt)

# ------------------------------------------------------------
# 7) 문자열 정렬 (sorted)
# ------------------------------------------------------------
strdata = input('\n정렬할 문자열을 입력하세요: ')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print('오름차순:', ret1)
print('내림차순:', ret2)

ret1 = ''.join(ret1)
ret2 = ''.join(ret2)
print('오름차순 정렬 결과:', ret1)
print('내림차순 정렬 결과:', ret2)

# ─────────────────────────────────────────────────────────────
# 8) 숫자에 3자리 콤마 넣기 (문자열 뒤집기 활용)
# ─────────────────────────────────────────────────────────────
num = input('\n아무 숫자를 입력하세요: ')
if num.isdigit():
    num_rev = num[::-1]
    ret = ''
    for i, c in enumerate(num_rev, start=1):
        if i != len(num_rev) and i % 3 == 0:
            ret += c + ','
        else:
            ret += c
    ret = ret[::-1]
    print('[3자리 콤마] →', ret)
else:
    print('입력한 내용 [%s]: 숫자가 아닙니다.' % num)

# ─────────────────────────────────────────────────────────────
# 9) 문자열 회전(rotate) — 다음 글자로 한 칸 이동
# ─────────────────────────────────────────────────────────────
text = input('\n문장을 입력하세요: ')
rotated = ''
for i in range(len(text)):
    rotated += text[i + 1] if i != len(text) - 1 else text[0]
print('[회전 결과] →', rotated)

# ─────────────────────────────────────────────────────────────
# 10) URL 파싱: 도메인과 쿼리 파라미터 나누기 (split)
# ─────────────────────────────────────────────────────────────
url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('/')
domain = tmp[2]
print('\n[도메인]', domain)

tmp = url.split('?')
queries = tmp[1].split('&')
print('[쿼리 파라미터]')
for query in queries:
    print(' -', query)
