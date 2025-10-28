"""
15_standard_modules.py
- 표준 모듈(time) 사용 예시
"""
import time                                   # 표준 라이브러리 time 모듈 임포트

def main():
    print('3초간 프로그램을 정지합니다.')          # 안내 메시지
    time.sleep(3)                              # 3초 대기(블로킹)
    print('3초가 지나갔습니다.')                 # 재개 후 메시지

if __name__ == "__main__":
    main()
