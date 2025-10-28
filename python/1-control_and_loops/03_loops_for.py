"""
03_loops_for.py
- for 반복문 기본 구조
- continue, break, else 사용
"""

def main():
    scope = [1, 2, 3, 4, 5]             # 반복할 리스트 정의
    print("[기본 for문]")
    for x in scope:                     # 리스트 요소를 하나씩 x에 대입
        print(x)                        # 1,2,3,4,5 순서로 출력

    print("\n[continue/break 예시]")
    for x in scope:
        print(x)
        if x < 3:                       # 3보다 작으면
            continue                    # 아래 코드를 건너뛰고 다음 반복으로 이동
        else:
            break                       # 3 이상이 되면 반복문 종료

    print("\n[for-else 구조]")
    scope2 = [1, 2, 3]
    for x in scope2:
        print(x)
    else:
        print('Perfect')                # for문이 정상 종료되면 실행됨

if __name__ == "__main__":
    main()
