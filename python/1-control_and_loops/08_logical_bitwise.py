"""
08_logical_and_bitwise.py
- 불리언 비교/논리 연산
- 비트 연산(&, |, ^, <<, >>)
"""

def main():
    # 불리언과 비교
    a = True
    b = False
    print(a == 1)                        # True == 1 → True (파이썬에선 bool은 int의 서브타입)
    print(b != 0)                        # False != 0 → False

    x = 1; y = 2
    str1 = 'abc'; str2 = 'python'
    print(x == y)                        # 숫자 비교(==)
    print(x != y)                        # 숫자 비교(!=)
    print(str1 == str2)                  # 문자열 비교(사전식 비교)
    print(str2 == 'python')              # 동일 문자열 → True
    print(str1 < str2)                   # 'abc' < 'python' (사전식)

    # 논리 연산
    bool1 = True; bool2 = False; bool3 = True; bool4 = False
    print(bool1 and bool2)               # 둘 다 True일 때만 True
    print(bool1 and bool3)               # True and True → True
    print(bool2 or bool3)                # 하나라도 True면 True
    print(bool2 or bool4)                # 모두 False → False
    print(not bool1)                     # True의 부정 → False
    print(not bool2)                     # False의 부정 → True

    # 비트 연산 예시 (정수 값의 비트 단위 연산)
    bit1 = 0x61                          # 0b0110_0001 (97)
    bit2 = 0x62                          # 0b0110_0010 (98)
    print(hex(bit1 & bit2))              # AND 공통 비트만 남김 → 0x60
    print(hex(bit1 | bit2))              # OR  하나라도 1이면 1 → 0x63
    print(hex(bit1 ^ bit2))              # XOR 다르면 1 → 0x3
    print(hex(bit1 >> 1))                # 오른쪽 시프트(2로 나눈 효과) → 0x30
    print(hex(bit1 << 2))                # 왼쪽 시프트(2비트 확장) → 0x184

if __name__ == "__main__":
    main()
