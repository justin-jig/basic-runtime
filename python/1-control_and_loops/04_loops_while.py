"""
04_loops_while.py
- while 반복문 기본 구조
- continue / break 제어문
"""

def main():
    x = 0                                # 초기값 설정
    while x < 10:                        # 조건이 True일 동안 반복
        x = x + 1                        # x에 1씩 더함 (x = 1 ~ 10)
        if x < 3:                        # 3보다 작으면
            continue                     # 아래 코드 건너뛰고 반복 계속
        print(x)                         # 3 이상일 때만 출력
        if x > 7:                        # x가 7보다 크면
            break                         # 반복문 종료

if __name__ == "__main__":
    main()
