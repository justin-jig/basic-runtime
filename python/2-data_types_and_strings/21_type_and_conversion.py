"""
21_type_and_conversion.py
- type()으로 데이터 타입 확인
- %d 포맷 문자열로 출력
- 이진수/16진수 변환(bin/hex, int())
"""

def func():
    print('안녕하세요.')

def main():
    # 타입 확인
    numdata = 57
    strdata = '파이썬'
    listdata = [1, 2, 3]
    dictdata = {'a':1, 'b':2}
    print(type(numdata))                    # <class 'int'>
    print(type(strdata))                    # <class 'str'>
    print(type(listdata))                   # <class 'list'>
    print(type(dictdata))                   # <class 'dict'>
    print(type(func))                       # <class 'function'>

    # %d 포맷 예시
    a = 11113
    b = 23
    ret = a % b
    print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.' % (a, b, ret))  # 정수 포맷

    # 16진수 변환
    h1 = hex(97)                            # '0x61'
    h2 = hex(98)                            # '0x62'
    print(h1 + ' ' + h2)                    # 문자열로 표시
    a16 = int(h1, 16)                       # 16진 문자열 → 10진 정수
    b16 = int(h2, 16)
    print(hex(a16 + b16))                   # 두 값 합의 16진수 표현

    # 2진수 변환
    b1 = bin(97)                            # '0b1100001'
    b2 = bin(98)                            # '0b1100010'
    print(b1 + ' ' + b2)                    # 문자열로 표시
    a2 = int(b1, 2)                         # 2진 문자열 → 정수
    b2i = int(b2, 2)
    print(bin(a2 + b2i))                    # 합의 2진수 표현

if __name__ == "__main__":
    main()
