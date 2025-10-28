"""
19_exception_advanced.py
- try-except-else : 예외 없을 때만 else 실행
- try-except-finally : 예외와 무관하게 finally 실행
- Exception as e : 실제 예외 메시지 확인
- KeyboardInterrupt : Ctrl+C 안전 처리
"""

import time                                  # sleep() 사용용

def demo_else():
    try:
        print('안녕하세요.')
        print('정상 흐름입니다.')            # 예외 없음
    except:
        print('예외가 발생했습니다!')
    else:
        print('예외가 발생하지 않았습니다.')  # except가 실행되지 않았을 때만 실행

def demo_finally():
    try:
        print('안녕하세요.')
        print(param)                          # NameError 발생
    except:
        print('예외가 발생했습니다!')
    finally:
        print('무조건 실행하는 코드')          # 예외 유무와 상관없이 항상 실행

def demo_exception_object():
    try:
        1 / 0                                 # ZeroDivisionError 발생
    except Exception as e:
        print('구체적 예외 메시지:', e)        # 예외 객체 출력으로 디버깅에 도움

def demo_keyboard_interrupt():
    count = 1
    try:
        while True:                           # 무한 루프
            print(count)                      # 현재 카운트 출력
            count += 1
            time.sleep(0.5)                   # 0.5초 대기
    except KeyboardInterrupt:                 # 사용자 Ctrl+C 입력 시
        print('사용자에 의해 프로그램이 중단되었습니다.')

if __name__ == "__main__":
    demo_else()
    demo_finally()
    demo_exception_object()
    # demo_keyboard_interrupt()              # 필요 시 주석 해제해 Ctrl+C 테스트
