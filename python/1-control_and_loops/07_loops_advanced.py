"""
07_loops_advanced.py
- 누적합 계산과 break로 조기 종료
"""

def main():
    x = 1                                # 더할 시작 값
    total = 0                            # 누적합 초기화
    while True:                          # 무한 루프(조건은 내부에서 제어)
        total = total + x                # x를 누적합에 더함
        if total > 100000:               # 누적합이 100000 초과하면
            print(x)                     # 마지막으로 더한 값 출력
            print(total)                 # 현재 누적합 출력
            break                        # 루프 종료
        x = x + 1                        # 다음 값으로 증가

if __name__ == "__main__":
    main()
