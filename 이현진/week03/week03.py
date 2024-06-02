#####################################################
# 예외처리
'''
try:
    print(10/0)
except ZeroDivisionError:
    print(10)
'''
# 더 쉬운방법(epsilon)
# lim i = 0에 수렴
# print(int(10 / 0.00000000000000000000000000001))


#####################################################
# 계산기
# 클래스 정의

#'''
class calculater_1:
    # 함수 정의
    def add(a, b):  # +
        return a + b

    def div(a, b):  # /
        try:
            return a / b
        except ZeroDivisionError:
            return a

    def mul(a, b):  # *
        return a * b

    def sub(a, b):  # -
        return a - b

print(calculater_1.add(4, 2))
print(calculater_1.div(4, 2))
print(calculater_1.mul(4, 2))
print(calculater_1.sub(4, 2))
#'''

#'''
class calculater_2:
    '''
    계산기 클래스
    '''
    # 함수 정의
    # 클래스 초기화
    def __init__(self):
        pass
    
    def add(self, a: float, b: float) -> float:  # +
        '''
        # JSDoc
        @param float a: 첫번째 매개변수
        @param float b: 두번째 매개변수
        @return float result: 더하기 결과
        '''
        result = a + b
        return result

    def div(self, a: float, b: float) -> float:  # /
        '''
        @param float a: 첫번째 매개변수
        @param float b: 두번째 매개변수
        @return float result: 나누기 결과
        '''
        result = a / b
        try:
            return result
        except ZeroDivisionError:
            return a

    def mul(self, a: float, b: float) -> float:  # *
        '''
        @param float a: 첫번째 매개변수
        @param float b: 두번째 매개변수
        @return float result: 곱하기 결과
        '''
        result = a * b
        return result

    def sub(self, a: float, b: float) -> float:  # -
        '''
        @param float a: 첫번째 매개변수
        @param float b: 두번째 매개변수
        @return float result: 빼기 결과
        '''
        result = a - b
        return result

    

# main 함수 역할
if __name__ == "__main__":
    c = calculater_2()
    a, b = map(int, input().split())
    print(c.add(a, b))
    print(c.div(a, b))
    print(c.mul(a, b))
    print(c.sub(a, b))
#'''

#####################################################
# 기본값 설정
def qwer(a = 10):
    print(a)
    
qwer(100)   # 100 출력
qwer()      # 10 출력
#####################################################

'''
HelloWorld 클래스
생성자:문자열 받기
helloCopy 메소드: 정수를 받아, 문자열을 * 정수만큼 가로로 출력
helloCopy2 메소드: 정수를 받아, 문자열을 * 정수만큼 세로로
helloReverse 메소드 : 아무것도 안받고 뒤집어서 출력
helloRectangle 메소드: 문자열을 정수만큼 가로, 세로 출력

단
주석 다달고, 타입 힌트 다 달고, 테스트 코드 작성
'''