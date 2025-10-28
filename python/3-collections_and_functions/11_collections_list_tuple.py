"""
11_collections_list_tuple.py
- 리스트(list)/튜플(tuple) 구조 비교
- 가변성(list는 수정 가능, tuple은 불변)
- 함수도 원소로 담을 수 있음
"""

def hello():
    print('안녕하세요')                              # 호출 시 인사 출력

def main():
    # 리스트(list) — 가변(mutable)
    list1 = [1, 2, 3, 4, 5]                        # 정수 리스트
    list2 = ['a', 'b', 'c']                        # 문자열 리스트
    list3 = [1, 'a', 'abc', [1,2,3], ['a','b','c']] # 다양한 타입 혼합 가능
    list1[0] = 6                                   # 리스트는 원소 수정 가능
    print(list1)                                   # [6, 2, 3, 4, 5]

    list4 = [1, 2, hello]                          # 함수도 원소로 저장 가능
    list4[2]()                                     # 저장된 함수 호출 → '안녕하세요'

    # 튜플(tuple) — 불변(immutable)
    tuple1 = (1, 2, 3, 4, 5)                       # 정수 튜플
    tuple2 = ('a', 'b', 'c')                       # 문자열 튜플
    tuple3 = (1, 'a', 'abc', [1,2,3], ['a','b','c']) # 내부에 리스트 포함 가능(자체는 불변)
    # tuple1[0] = 6                                 # ❌ 오류: 튜플은 원소 변경 불가

    tuple4 = (1, 2, hello)                         # 튜플에도 함수 담기 가능
    tuple4[2]()                                    # 함수 호출 → '안녕하세요'

if __name__ == "__main__":
    main()
