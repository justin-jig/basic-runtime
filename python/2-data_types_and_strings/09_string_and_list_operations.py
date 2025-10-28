"""
09_string_and_list_operations.py
- 문자열/리스트 인덱싱, 슬라이싱
- 문자열/리스트 연결(+)
"""

def main():
    # 인덱싱(양수: 앞에서, 음수: 뒤에서)
    strdata = 'Time is money!!'         # 인덱스: 0..len-1
    listdata = [1, 2, [1, 2, 3]]        # 중첩 리스트
    print(strdata[5])                   # 5번째 문자 → 'i'
    print(strdata[-2])                  # 끝에서 2번째 → '!'
    print(listdata[0])                  # 0번째 원소 → 1
    print(listdata[-1])                 # 마지막 원소 → [1,2,3]
    print(listdata[2][-1])              # 중첩 리스트의 마지막 원소 → 3

    # 슬라이싱(시작:끝:스텝) — 끝 인덱스는 포함되지 않음
    print(strdata[1:5])                 # 1~4번째 문자 → 'ime '
    print(strdata[:7])                  # 처음~6 → 'Time is'
    print(strdata[9:])                  # 9~끝 → 'oney!!'
    print(strdata[:-3])                 # 처음~끝-3 → 'Time is mone'
    print(strdata[-3:])                 # 끝-3~끝 → 'y!!'
    print(strdata[:])                   # 전체 복사
    print(strdata[::2])                 # 2칸씩 건너뛰며 추출

    # 연결(+) — 새 객체를 만들어 반환
    strdata1 = 'I love '; strdata2 = 'Python'; strdata3 = 'you'
    listdata1 = [1, 2, 3]; listdata2 = [4, 5, 6]
    print(strdata1 + strdata2)          # 'I love Python'
    print(strdata1 + strdata3)          # 'I love you'
    print(listdata1 + listdata2)        # [1,2,3,4,5,6]

if __name__ == "__main__":
    main()
