"""
18_exception_handling.py
- 기본 try-except 구조
- 예외 발생 시 안전하게 처리
"""

def main():
    try:
        print('안녕하세요.')                 # 정상 실행 코드
        print(param)                        # 정의되지 않은 변수 접근 → NameError 발생
    except:
        print('예외가 발생했습니다!')        # 어떤 예외든 잡아서 사용자 메시지 출력

if __name__ == "__main__":
    main()
