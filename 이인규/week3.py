'''python
HelloWorld 클래스
생성자: 문자열을 받아
helloCopy 메소드: 정수를 받아, 문자열을 * 정수 만큼 가로로 출력
helloCopy2 메소드: 정수를 받아, 문자열을 * 정수 만큼 세로로 출력
helloReverse 메소드: 아무것도 안받아, 그냥 뒤집어서 출력
helloRectangle 메소드: 정수를 받아, 문자열을 * 정수만큼 가로, 세로 출력

단.
주석 다달고, 타입 힌트 다달고, 테스트 코드 작성
'''

class calculater:
    '''이 클래스 계산기 클래스야
    '''
    
    def __init__(self):
        pass

    def add(self, a: float, b: float) -> float:
        '''
        @param float a: 첫번째 매개변수
        @param float b: 두번째 매개변수
        @return float result: 더하기 결과값
        '''
        result = a + b

        return result

    def div(self, a: float, b: float) -> float:
        try:
            result = a / b
        except ZeroDivisionError:
            result = a

        return result

    def mul(self, a: float, b: float) -> float:
        result = a * b

        return result

    def sub(self, a: float, b: float) -> float:
        result = a - b

        return result

if __name__ == "__main__":
    c = calculater()
    a, b = map(int, input().split())

    print(c.add(a, b))
    print(c.div(a, b))
    print(c.mul(a, b))
    print(c.sub(a, b))

c.add(1, 10)
