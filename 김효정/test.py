#try:
#    a = 10 / 0
#except ZeroDivisionError:
#    print(10)

#print(int(10/0.000000000000000000000001))

class calculater:
    '''이 클래스는 계산기 클래스야'''
    def __init__(self):
        pass

    def add(self, a:float, b:float) -> float:  #더하기
        '''@param float a : 첫번째 변수
        @param float b : 두번때 변수
        @return float result : 반환 변수'''

        result = a+b
        return result
    def sub(self, a:float, b:float) -> float:  #빼기
        '''@param float a : 첫번째 변수
        @param float b : 두번때 변수
        @return float result : 반환 변수'''
        result = a-b
        return result
    def mul(self, a:float, b:float) -> float:  #곱하기
        '''@param float a : 첫번째 변수
        @param float b : 두번때 변수
        @return float result : 반환 변수'''
        result = a*b
        return result
    def div(self, a:float, b:float) -> float:  #나누기
        '''@param float a : 첫번째 변수
        @param float b : 두번때 변수
        @return float result : 반환 변수'''
        try:
            result = a/b
        except ZeroDivisionError:
            return a
        result = a/b
        return result

a, b = input().split()
a = int(a)
b = int(b)

cal = calculater()

print(cal.add(a, b))
print(cal.sub(a, b))
print(cal.mul(a, b))
print(cal.div(a, b))

cal.add