"""
16_class_basics.py
- 클래스 정의/속성/메서드
- self(인스턴스 자신)와 지역변수 차이
- 생성자(__init__)
"""

# 1) 기본 클래스 구조
class MyClass1:
    var = '안녕하세요'                          # 클래스 변수(모든 인스턴스가 공유)
    def sayHello(self):                        # 인스턴스 메서드(첫 인자는 항상 self)
        print(self.var)                        # self.var로 인스턴스/클래스 속성 접근

# 2) self vs 지역변수
class MyClass2:
    var = '안녕하세요!!'
    def sayHello(self):
        param1 = '안녕'                        # 지역 변수(메서드 호출 끝나면 소멸)
        self.param2 = '하이'                   # 인스턴스 변수(인스턴스에 저장)
        print(param1)                          # 지역변수 출력
        print(self.var)                        # 클래스/인스턴스 속성 출력

# 3) 메서드 인자 전달
class MyClass3:
    def sayHello(self):
        print('안녕하세요')                     # 인자 없는 메서드
    def sayBye(self, name):
        print(f'{name}! 다음에 보자!')          # 인자 있는 메서드

# 4) 생성자(__init__)
class MyClass4:
    def __init__(self):                        # 인스턴스 생성 시 자동 호출
        self.var = '안녕하세요!'                 # 인스턴스 속성 초기화
        print('MyClass 인스턴스 객체가 생성되었습니다')

def main():
    obj1 = MyClass1()                          # 인스턴스 생성
    print(obj1.var)                            # '안녕하세요' 출력
    obj1.sayHello()                            # 메서드 호출

    obj2 = MyClass2()
    obj2.sayHello()                            # 지역/인스턴스 변수 차이 확인

    obj3 = MyClass3()
    obj3.sayHello()                            # '안녕하세요'
    obj3.sayBye('철수')                        # '철수! 다음에 보자!'

    obj4 = MyClass4()                          # 생성자 메시지 출력
    print(obj4.var)                            # 생성자에서 설정한 값 확인

if __name__ == "__main__":
    main()
