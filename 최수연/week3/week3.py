class calculator:
    '''
    이 클래스는 계산기 클래스야
    '''
    def __init__(self):
        pass

    def add(self, A: float, B: float) -> float:
        '''
        @param float A: 첫번째 매개변수
        @param float B: 두번째 매개변수
        @return float result: 더하기 결과
        '''
        result = A + B
        return result

    def div(self, A: float, B: float) -> float:
        '''
        @param float A: 첫번째 매개변수
        @param float B: 두번째 매개변수
        @return float result: 나누기 결과
        '''
        try:
            result = A / B
            return result
        except ZeroDivisionError:
            result = A

    def  mul(self, A: float, B: float) -> float:
        '''
        @param float A: 첫번째 매개변수
        @param float B: 두번째 매개변수
        @return float result: 곱하기 결과
        '''
        result = A * B
        return result

    def sub(self, A: float, B: float) -> float:
        '''
        @param float A: 첫번째 매개변수
        @param float B: 두번째 매개변수
        @return float result: 빼기 결과
        '''
        result = A - B
        return result

if __name__ == "__main__":
    c = calculator()
    A, B = map(int, input().split())

    print(c.add(A, B))
    print(c.div(A, B))
    print(c.mul(A, B))
    print(c.sub(A, B))
    


