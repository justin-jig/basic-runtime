"""
02_conditionals.py
- if, elif, else 조건문 사용
- in 연산자(리스트 내 포함 여부)
"""

def main():
    x = 1                               # 변수 x에 1 저장
    y = 2                               # 변수 y에 2 저장

    if x > y:                           # 조건: x가 y보다 크면
        print('x가 y보다 큽니다.')
    elif x < y:                         # 조건: x가 y보다 작으면
        print('x가 y보다 작습니다.')
    else:                               # 위 조건 모두 아닐 때
        print('x와 y가 같습니다.')

    # in 연산자 : 특정 값이 리스트에 존재하는지 검사
    listdata = ['a', 'b', 'c']
    if 'a' in listdata:                 # 'a'가 리스트에 포함되어 있으면
        print('a가 listdata에 있습니다.')
        print(listdata)
    else:
        print('a가 listdata에 존재하지 않습니다.')

if __name__ == "__main__":
    main()
