#HelloWorld 클래스 만들기
#생성자 : 문자열 받기
#HelloCopy1 메서드: 정수를 받아, 문자열을 *정수 만큼 가로로 출력
#HelloCopy2 메서드: 정수를 받아, 문자열을 *정수 만큼 세로로 출력
#HelloReverse 메서드 : 아무것도 안받아, 그냥 뒤집어서 출력
#HelloRectangle 메서드 : 정수를 받아, 문자열을 *만큼 가로, 세로 출력
#주석 달기, 타입 힌트 달기, 테스트 코드 작성
class calculater :
    '''이 클래스는 계산기 클래스입니다.'''
    def __init__(self):
       '''이 함수는 초기화 함수입니다.'''
       pass

    def add(self, A:float,B:float)->float:
        '''
        이 함수는 덧셈 함수입니다.
        @param float a:첫번째 매개변수
        @param float b:두번째 매개변수
        @param float c:덧셈 결과값
        '''
        result=A+B
        return result

    def div(self, A:float,B:float)->float:
        '''
        이 함수는 나눗셈 함수입니다.
        @param float a:첫번째 매개변수
        @param float b:두번째 매개변수
        
        '''
        try:
          result=A/B
          return result
        except ZeroDivisionError:
          return A

    def mul(self, A:float,B:float)->float:
        '''
        이 함수는 곱셈 함수입니다.
        @param float a:첫번째 매개변수
        @param float b:두번째 매개변수
        @param float c:곱셈 결과값
        '''
        result=A*B
        return result

    def sub(self, A:float,B:float)->float:
        '''
        이 함수는 뺄셈 함수입니다.
        @param float a:첫번째 매개변수
        @param float b:두번째 매개변수
        @param float c:뺄셈 결과값
        '''
        result=A-B
        return result

if __name__=="__main__":
    c=calculater()
    A,B=map(int,input().split(" "))
    print(c.add(A,B))
    print(c.sub(A,B))
    print(c.div(A,B))
    print(c.mul(A,B))