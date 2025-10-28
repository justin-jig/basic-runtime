# 36_functional_and_sorting.py
# 딕셔너리 정렬, lambda 함수, eval, map, 문자 코드 변환

# ------------------------------------------------------------
# 1) 딕셔너리 정렬 (sorted + key 함수)
# ------------------------------------------------------------
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly':7855}

# 기본 정렬 (키 기준)
ret1 = sorted(names)
print('[기본 키 정렬]:', ret1)

# 사용자 정의 함수 사용
def f1(x): return x[0]  # 키 기준
def f2(x): return x[1]  # 값 기준

ret2 = sorted(names.items(), key=f1)
print('\n[f1 키 기준 정렬]:', ret2)

ret3 = sorted(names.items(), key=f2)
print('[f2 값 기준 정렬]:', ret3)

ret4 = sorted(names.items(), key=f2, reverse=True)
print('[값 기준 내림차순 정렬]:', ret4)

# lambda를 사용한 키 정렬
ret5 = sorted(names.items(), key=lambda x: x[0])
print('[lambda 키 기준 정렬]:', ret5)

# ------------------------------------------------------------
# 2) 문자 코드 변환 (ord, chr)
# ------------------------------------------------------------
val = input('\n문자 코드값을 입력하세요: ')
val = int(val)
try:
    ch = chr(val)
    print('코드값: %d [%s], 문자: %s' % (val, hex(val), ch))
except ValueError:
    print('입력한 <%d>에 대한 문자가 존재하지 않습니다!' % val)

ch = input('\n문자를 1개 입력하세요: ')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자: %s \t코드값: %d [%s]' % (ch, chv, hex(chv)))

# ------------------------------------------------------------
# 3) eval() - 문자열 표현식 계산
# ------------------------------------------------------------
expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('\n[eval()] 실행 결과:')
print(f'{expr1} → {ret1}')
print(f'{expr2} → {ret2}')

# ------------------------------------------------------------
# 4) lambda / map 사용 예제
# ------------------------------------------------------------
add = lambda x, y: x + y
print('\n[lambda] add(1,3) =', add(1, 3))

funcs = [lambda x: x + '.pptx', lambda x: x + '.docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

f = lambda x: x * x
args = [1, 2, 3, 4, 5]
ret = map(f, args)
print('\n[map()] 제곱 결과:', list(ret))
