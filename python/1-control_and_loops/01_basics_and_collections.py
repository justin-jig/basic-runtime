"""
01_basics_and_collections.py
- 기본 출력(print), 변수 사용
- 리스트(list) / 딕셔너리(dict) 다루기
"""

def main():
    print("안녕하세요")                 # 콘솔에 문자열 출력
    a = 1                              # 변수 a에 정수 1 저장
    b = 1                              # 변수 b에 정수 1 저장
    print(a + b)                       # a와 b의 합(2)을 출력

    a = 200                            # 정수 변수
    msg = 'I love Python'              # 문자열 변수
    list_data = ['a', 'b', 'c']        # 리스트 자료형 (순서 있는 데이터)
    dict_data = {'a': 97, 'b': 98}     # 딕셔너리 자료형 (키-값 쌍으로 저장)

    print(a)                           # 정수 200 출력
    print(msg)                         # 문자열 'I love Python' 출력
    print(list_data)                   # 리스트 전체 ['a', 'b', 'c'] 출력
    print(list_data[0])                # 리스트의 첫 번째 원소 'a' 출력
    print(dict_data)                   # 딕셔너리 전체 출력
    print(dict_data['a'])              # 키 'a'에 해당하는 값 97 출력

if __name__ == "__main__":
    main()
