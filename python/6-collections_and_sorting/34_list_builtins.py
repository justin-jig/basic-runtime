# 34_list_builtins.py
# 리스트 내장 함수 (sum, all, any) 활용 예제

# ------------------------------------------------------------
# 1) sum() - 리스트 요소의 합계
# ------------------------------------------------------------
listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
ret = sum(listdata)
print('[sum] 합계 결과:', ret)  # 65 출력

# ------------------------------------------------------------
# 2) all(), any() - 참/거짓 평가
# ------------------------------------------------------------
listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]

print('\n[all / any 테스트]')
print('listdata1 all:', all(listdata1))  # False (0 존재)
print('listdata1 any:', any(listdata1))  # True  (0 외 True 값 존재)
print('listdata2 all:', all(listdata2))  # True  (모두 True)
print('listdata2 any:', any(listdata2))  # True
print('listdata3 all:', all(listdata3))  # False (모두 False)
print('listdata3 any:', any(listdata3))  # False (하나도 True 없음)
