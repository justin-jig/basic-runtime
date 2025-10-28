# 문자열에서 짝수 인덱스 문자 추출
# 슬라이싱: [start:end:step] 문법 사용

txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2]  # step=2 → 짝수 인덱스만 선택
print(ret)  # ‘abcdefghijk’ 출력
