"""
10_string_advanced.py
- 문자열 결합/반복/길이/멤버십
- 서식 지정(% 포매팅)
- 특수문자 이스케이프
"""

def main():
    # 결합/반복
    artist = '빅뱅'                                  # 가수 이름 문자열
    sing = '뱅~'                                     # 후렴 문자열
    dispdata = artist + '이 부르는 ' + sing * 3      # +로 결합, *로 반복
    print(dispdata)                                  # '빅뱅이 부르는 뱅~뱅~뱅~'

    # 길이와 멤버십(in)
    strdata1 = 'I love python'
    strdata2 = '나는 파이썬을 사랑합니다'
    listdata = ['a', 'b', 'c', strdata1, strdata2]
    print(len(strdata1))                             # 문자열 길이(공백 포함)
    print(len(strdata2))                             # 한글도 문자 단위 길이
    print(len(listdata))                             # 리스트 원소 개수
    print(len(listdata[3]))                          # 리스트 3번 원소(문자열)의 길이

    listdata2 = [1, 2, 3, 4]
    print(5 in listdata2)                            # 리스트에 5가 있는가? → False
    print(4 in listdata2)                            # 리스트에 4가 있는가? → True
    txt = 'abcde'
    print('c' in txt)                                # 문자열 포함 여부 → True
    print('1' in txt)                                # '1'은 없음 → False

    # % 포매팅 (레거시 방식) — %s(문자열), %d(정수), %%('%' 자체)
    txt1 = '자바'; txt2 = '파이썬'
    num1 = 5; num2 = 10
    print('나는 %s보다 %s에 더 익숙합니다.' % (txt1, txt2))        # 다중 치환
    print('%s은 %s보다 %d배 더 쉽습니다.' % (txt2, txt1, num1))   # %d는 정수
    print('%d + %d = %d' % (num1, num2, num1 + num2))             # 계산 결과 포매팅
    print('성장률은 전년 대비 %d%% 증가.' % num1)                 # %% → '%' 문자

    # 특수문자 이스케이프
    print('첫째 줄\n둘째 줄')                                       # \n 줄바꿈
    print('A\tB\tC')                                              # \t 탭
    print('역슬래시는 이렇게 씁니다: \\\\')                          # \\ → \ 출력
    print('작은따옴표(\')와 큰따옴표(\") 모두 가능')                   # 따옴표 이스케이프

if __name__ == "__main__":
    main()
