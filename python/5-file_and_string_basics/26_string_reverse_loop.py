# 문자열 뒤집기 (for 루프 방식)
# range()로 인덱스 접근하며 직접 역순 결합

txt = 'abcdefghijk'
ret = ''
for i in range(len(txt)):
    ret += txt[-(i + 1)]  # 끝에서부터 한 글자씩 추가
print(ret)  # ‘kjihgfedcba’
