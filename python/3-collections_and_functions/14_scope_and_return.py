"""
14_scope_and_return.py
- 지역/전역 변수와 global
- 다중 반환값과 언패킹
"""

param = 10                                   # 전역 변수(모듈 전체에서 접근 가능)
strdata = '전역변수'                           # 전역 문자열

def func1():
    strdata = '지역변수'                       # 같은 이름의 지역변수(전역과 다른 별개)
    print(strdata)                            # 지역 스코프의 strdata를 출력

def func2(p):
    p = 1                                     # 값 타입(숫자) 재할당 → 호출자 변수에 영향 없음

def func3():
    global param                              # 전역변수 param을 사용하겠다고 선언
    param = 50                                # 전역 param 값을 50으로 변경

def reverse(x, y, z):
    return z, y, x                            # 여러 값을 튜플로 반환

def main():
    func1()                                   # '지역변수' 출력
    print(strdata)                            # 전역 '전역변수' 출력
    print(param)                              # 전역 param(10) 출력

    func2(param)                              # 호출자 입장에선 param 그대로(불변)
    print(param)                              # 여전히 10

    func3()                                   # 전역 param을 50으로 바꿈
    print(param)                              # 50 출력

    ret = reverse(1, 2, 3)                    # (3, 2, 1) 튜플 반환
    print(ret)                                # 튜플 그대로 출력
    r1, r2, r3 = reverse('a', 'b', 'c')       # 언패킹: r1='c', r2='b', r3='a'
    print(r1); print(r2); print(r3)

if __name__ == "__main__":
    main()
