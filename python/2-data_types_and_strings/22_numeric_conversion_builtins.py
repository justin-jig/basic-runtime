"""
22_numeric_conversion_and_builtins.py
- int()/float() 변환
- 진법 문자열을 int로 변환(base 지정)
- abs() 절대값
"""

def main():
    # 진법 문자열을 int로 변환
    bnum = 0b11110000; bstr = '0b11110000'  # 정수/문자열(2진 표기)
    onum = 0o360;       ostr = '0o360'      # 정수/문자열(8진 표기)
    hnum = 0xf0;        hstr = '0xf0'       # 정수/문자열(16진 표기)

    b1 = int(bnum)                           # 이미 정수면 그대로 int
    b2 = int(bstr, 2)                        # 2진 문자열 → 정수
    o1 = int(onum)                           # 8진 정수 그대로
    o2 = int(ostr, 8)                        # 8진 문자열 → 정수
    h1 = int(hnum)                           # 16진 정수 그대로
    h2 = int(hstr, 16)                       # 16진 문자열 → 정수
    print(b1, b2); print(o1, o2); print(h1, h2)

    # abs() : 절대값(정수/실수/복소수 모두 가능)
    print(abs(-3))                           # 3
    print(abs(-5.72))                        # 5.72
    print(abs(3+4j))                         # 5.0 (피타고라스: sqrt(3^2+4^2))

    # float()/int() 변환
    print(float(10))                         # 10.0 (정수 → 실수)
    print(int(-5.4))                         # -5   (소수점 버림)
    print(int(1.78e1))                       # 17   (지수표기 → 정수 변환)
    print(int(171.56))                       # 171  (소수점 버림)

if __name__ == "__main__":
    main()
