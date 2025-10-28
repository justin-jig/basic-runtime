"""
23_builtins_bitwise_and_indexing.py
- filter()로 조건에 맞는 값만 추려내기
- max()/min() 최댓/최솟값
- 비트 AND/시프트로 마스킹/니블 추출
- 문자열 인덱싱(양수/음수)
"""

def getPrime(x):
    # 소수면 x를 반환, 아니면 None(=Falsey)
    for i in range(2, x - 1):
        if x % i == 0:                     # 나눠떨어지면 합성수
            break
    else:
        return x                           # for가 break 없이 끝나면 소수

def main():
    # 1) filter() : 조건을 만족하는 원소만 남김
    listdata = [117, 119, 1113, 11113, 11119]
    ret = filter(getPrime, listdata)       # getPrime이 True(값 반환)인 것만 남음
    print(list(ret))                       # [11113, 11119]

    # 2) max()/min()
    listdata2 = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
    print(max(listdata2)); print(min(listdata2))   # 리스트의 최댓/최솟값
    txt = 'Alotofthingsoccureachday'
    print(max(txt)); print(min(txt))       # 문자 코드값 기준(사전식) 최댓/최솟
    print(max(2+3, 2*3, 2**3, 3**2))       # 여러 표현식 중 최댓값 → 9
    print(min('abz', 'a12'))               # 문자열 비교 → 'abz'가 더 큼/작음에 유의

    # 3) 비트 연산 — 하위 4비트(니블) 마스킹/시프트
    a = 107                                # 0x6B (2진수 0110 1011)
    b = a & 0x0F                           # 하위 4비트만 남기기(AND 마스크)
    print(hex(b))                          # 0xb

    b2 = (a >> 4) & 0x0F                   # 상위 니블 추출: 4비트 우시프트 후 마스킹
    print(b2)                              # 6

    # 4) 문자열 인덱싱
    txt1 = 'A tale that was not right'
    txt2 = '이 또한 지나가리라.'
    print(txt1[5])                         # 양수 인덱스(앞에서 6번째) → 'e'
    print(txt2[-2])                        # 음수 인덱스(뒤에서 2번째) → '다'

if __name__ == "__main__":
    main()
