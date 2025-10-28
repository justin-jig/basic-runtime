"""
13_functions_basics.py
- 함수 정의/호출/반환
- 기본값 인자, 키워드 인자
- 가변 인자(*args, **kwargs)
"""

def add_number(n1, n2):
    return n1 + n2                                  # 두 수의 합 반환

def add_txt(t1, t2):
    print(t1 + t2)                                  # 두 문자열을 이어서 출력

def add_txt_default(t1, t2='파이썬'):
    print(t1 + ' : ' + t2)                          # t2 기본값 사용(미지정 시 '파이썬')

def func1(*args):
    print(args)                                     # 위치 인자들을 튜플로 받음

def func2(width, height, **kwargs):
    print(kwargs)                                   # 키워드 추가 인자들을 dict로 받음

def main():
    ans = add_number(10, 15)                        # 10 + 15 계산
    print(ans)                                      # 25 출력

    add_txt('대한민국~', '만세!!')                   # 문자열 연결 출력
    add_txt_default('베스트')                        # 기본값 t2='파이썬' 사용
    add_txt_default(t2='대한민국', t1='1등')          # 키워드 인자로 순서 무관

    func1()                                         # 빈 튜플 출력 → ()
    func1(3, 5, 1, 5)                               # 전달된 인자들이 튜플로 출력
    func2(10, 20)                                   # 추가 키워드 인자 없음 → {}
    func2(10, 20, depth=50, color='blue')           # depth/color가 dict로 출력

if __name__ == "__main__":
    main()
