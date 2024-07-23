
class HelloWorld:
    '''
    다양한 방법으로 입력받은 문자열을 출력하는 클래스
    '''
    def __init__(self):
        pass

    def helloCopy(self, a: str, b: int):  
        '''
        @param str a: 첫번째 매개변수
        @param int b: 두번째 매개변수
        @입력받은 문자열을 입력받은 정수만큼 반복해서 한 줄에 출력하는 메서드
        '''  
        for i in  range(int(b)):
            print(a, end = "") # 파이썬에서는 줄바꿈이 기본이라 end = "" 로 한 줄에 작성
        print() # main에서 print없이 함수만 썼더니 다음문단으로 안 넘어가서 추가
        

    def helloCopy2(self, a: str, b: int):   
        '''
        @param str a: 첫번째 매개변수
        @param int b: 두번째 매개변수
        @입력받은 문자열을 입력받은 정수만큼 반복해서 출력하는 메서드
        ''' 
        for i in  range(int(b)):
            print(a)

    def helloReverse(self, a: str):
        '''
        @param str a: 매개변수
        @입력받은 문자열을 뒤집어서 출력하는 메서드
        '''
        '''
        슬라이싱(slicing): 연속된 객체들에 범위를 지정해 선택하여 객체들을 가져오는 방법

        기본형태: string[start:stop:step] 문자열[시작:끝:규칙]
            start: 슬라이싱을 시작할 위치 (기본값: 0)
            stop: 슬라이싱을 끝낼 위치 (주의! stop은 포함하지 않음) (기본값: 문자열의 끝)
            step: 몇개씩 끊어서 가져올지와 방향 설정 (음수면 좌측으로 양수면 우측으로) (기본값: 1)

        string:              h e l l o w o r l d
        positive indexing:   0 1 2 3 4 5 6 7 8 9 (좌측에서 0부터 시작)
        negative indexing: -10-9-8-7-6-5-4-3-2-1 (우측에서 -1부터 시작)
        
        ex) [3:7:] --> lowo
            [-4::] --> orld
            [:6:] --> hellow
            [-2::-3] --> lwl
            [8:1:-2] --> lool
        '''
        print(a[::-1]) # 문자열 전체를 좌측부터 1칸씩 이동하며 가져오기



    def helloRectangle(self, a: str, b: int):  
        '''
        @param str a: 첫번째 매개변수
        @param int b: 두번째 매개변수
        @입력받은 문자열을 입력받은 정수만큼 가로, 세로로 출력하는 메서드
        '''  
        for i in  range(int(b)):
            for i in  range(int(b)):
                print(a, end = "") 
            print() 
        # 한줄로 문자열 a를 b번 반복해서 작성후 줄바꿈 <--이걸 b번 만큼 반복



if __name__ == "__main__":
    h = HelloWorld()
    
    a, b = input().strip().split()

    h.helloCopy(a, b)
    h.helloCopy2(a, b)
    h.helloReverse(a)
    h.helloRectangle(a, b)
    #print했더니 None이 같이 출력돼서 print없이 함수만 작성 (return값이 없으면 그런다고 함)

    '''
    실행결과
    helloworld 3
    helloworldhelloworldhelloworld
    helloworld
    helloworld
    helloworld
    dlrowolleh
    helloworldhelloworldhelloworld
    helloworldhelloworldhelloworld
    helloworldhelloworldhelloworld
    '''
