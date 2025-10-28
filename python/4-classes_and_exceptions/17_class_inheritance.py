"""
17_class_inheritance.py
- 단일 상속과 다중 상속
- 부모 메서드 상속/재사용
"""

class Add:
    def add(self, n1, n2):
        return n1 + n2                         # 두 수 덧셈

class Calculator(Add):                         # 단일 상속: Add를 상속
    def sub(self, n1, n2):
        return n1 - n2                         # 뺄셈 기능 추가

class Multiply:
    def multiply(self, n1, n2):
        return n1 * n2                         # 곱셈

class AdvancedCalculator(Add, Multiply):       # 다중 상속: Add와 Multiply 모두 상속
    def sub(self, n1, n2):
        return n1 - n2                         # 뺄셈도 제공(자체 구현)

def main():
    obj = Calculator()                         # Calculator는 Add의 add() 사용 가능
    print(obj.add(1, 2))                       # 3
    print(obj.sub(1, 2))                       # -1

    obj2 = AdvancedCalculator()                # add/multiply/sub 모두 사용 가능
    print(obj2.add(1, 2))                      # 3
    print(obj2.multiply(3, 2))                 # 6

if __name__ == "__main__":
    main()
