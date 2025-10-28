"""
12_dictionary_basics.py
- 딕셔너리 생성/조회/수정
- 길이(len) 확인
"""

def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}               # 키:값 쌍으로 저장
    print(dict1['a'])                               # 키 'a'의 값 조회 → 1

    dict1['d'] = 4                                  # 새 키 'd' 추가
    print(dict1)                                    # {'a':1, 'b':2, 'c':3, 'd':4}

    dict1['b'] = 7                                  # 기존 키 'b'의 값 변경
    print(dict1)                                    # {'a':1, 'b':7, 'c':3, 'd':4}

    print(len(dict1))                               # 항목 수(키 개수) → 4

if __name__ == "__main__":
    main()
