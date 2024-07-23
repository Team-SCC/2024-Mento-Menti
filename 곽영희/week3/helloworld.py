#HelloWorld 클래스 만들기
#생성자 : 문자열 받기
#HelloCopy1 메서드: 정수를 받아, 문자열을 *정수 만큼 가로로 출력
#HelloCopy2 메서드: 정수를 받아, 문자열을 *정수 만큼 세로로 출력
#HelloReverse 메서드 : 아무것도 안받아, 그냥 뒤집어서 출력
#HelloRectangle 메서드 : 정수를 받아, 문자열을 *만큼 가로, 세로 출력
#주석 달기, 타입 힌트 달기, 테스트 코드 작성
class HelloWorld :
    '''이 클래스는 HelloWorld  클래스입니다.'''
    def __init__(self, string:str)->None:
       '''이 함수는 초기화 함수입니다.'''
       self.string=string

    def HelloCopy1(self, A:int)->str:
        '''
        이 함수는 정수를 받아, 문자열을 *정수 만큼 가로로 출력하는 함수입니다.
        @param int A:첫번째 매개변수
        @param str result:출력값
        '''
        result=A*'HelloWorld '
        return result

    def HelloCopy2(self, A:int)->str:
        '''
        정수를 받아, 문자열을 *정수 만큼 세로로 출력하는 함수입니다.
        @param int A:첫번째 매개변수
        @param str result:출력값
        '''
        result=A*'HelloWorld\n'
        return result

    def HelloReverse(self)->str:
        '''
        이 함수는 아무것도 안받아, 그냥 뒤집어서 출력하는 함수입니다.
        @param str result:출력값
        '''
        strings = "HelloWorld"
        reverse_string ="".join(reversed(strings))
        return reverse_string

    def HelloRectangle(self, A:int)->str:
        '''
        이 함수는 정수를 받아, 문자열을 *만큼 가로, 세로 출력하는 함수입니다.
        @param int A:첫번째 매개변수
        @param str result:출력값
        '''
        result1=(A*'HelloWorld ')+"\n"+(A*'HelloWorld\n')
        return result1

if __name__=="__main__":
    c=HelloWorld("Hello")
    A=int(input())
    print(c.HelloCopy1(A))
    print(c.HelloCopy2(A))
    print(c.HelloReverse())
    print(c.HelloRectangle(A))
