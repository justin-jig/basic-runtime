"""
06_operations_and_print.py
- print의 end 옵션
- 산술 연산자(+,-,*,/,**,())와 우선순위
"""

def main():
    # print의 end: 줄바꿈 대신 지정한 문자열로 끝내기
    a = 1; b = 2
    ret = a + b
    print('a와 b를 더한 값은 ', end='')  # 줄바꿈 없이 이어서 출력
    print(ret, end='')                   # 이어서 결과 출력
    print(' 입니다')                     # 마지막에 문장 마무리

    # 산술 연산 및 우선순위 확인
    a = 2
    b = 4
    ret1 = a + b                         # 덧셈
    ret2 = a - b                         # 뺄셈
    ret3 = a * b                         # 곱셈
    ret4 = a / b                         # 나눗셈(실수)
    ret5 = a ** b                        # 거듭제곱(2^4=16)
    ret6 = a + a * b / a                 # 곱셈/나눗셈이 덧셈보다 우선
    ret7 = (a + b) * (a - b)             # 괄호로 우선순위 강제
    ret8 = a * b ** a                    # **가 *보다 우선(b**a 먼저)
    print(ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8)

if __name__ == "__main__":
    main()
