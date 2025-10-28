"""
05_numeric_types.py
- 정수(int), 실수(float), 복소수(complex) 기본
- 지수표기(e 표기)와 실수부/허수부 확인
"""

def main():
    # 정수 리터럴(10진수/2진수/8진수/16진수)
    int_data = 10                      # 10진 정수
    bin_data = 0b10                    # 2진수(= 2)
    oct_data = 0o10                    # 8진수(= 8)
    hex_data = 0x10                    # 16진수(= 16)
    long_data = 1234567890123456789    # 파이썬 int는 임의정밀도(오버플로우 없음)

    print(int_data)                    # 10 출력
    print(bin_data)                    # 2 출력
    print(oct_data)                    # 8 출력
    print(hex_data)                    # 16 출력
    print(long_data)                   # 큰 정수 출력

    # 실수와 지수 표기
    f1 = 1.0                           # 기본 실수
    f2 = 3.14                          # 소수점 표기
    f3 = 1.56e3                        # 지수 표기(= 1560.0)
    f4 = -0.7e-4                       # 지수 표기(= -0.00007)
    print(f1, f2, f3, f4)              # 각각의 실수 값 출력

    # 복소수 (a + bj 형태)
    c1 = 1 + 7j                        # 실수부 1, 허수부 7
    print(c1.real); print(c1.imag)     # 실수부/허수부 출력
    c2 = complex(2, 3)                 # complex 생성자(2 + 3j)
    print(c2)                          # (2+3j) 출력

if __name__ == "__main__":
    main()
