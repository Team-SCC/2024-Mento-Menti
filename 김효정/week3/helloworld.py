class HelloWorld:
    '''이 클래스는 문자 출력? 클래스야'''
    def __init__(self, string:str):
        self.string = string

    def helloCopy(self, a: int, char: str) -> str:
        '''@param int a : 가로로 출력 횟수'''
        result = char * a
        print(result)
    
    def helloCopy2(self, a: int) -> None:
        '''@param int a : 반복 횟수'''
        for i in range(a):
            print("helloworld")
    
    def helloReverse(self) -> None:
        '''문자열을 뒤집어 출력'''
        char = "helloworld"
        r = ''

        for i in char:
            r = i + r

        print(r)

    def helloRectangle(self, a: int, char: str) -> None:
        '''주어진 문자열을 가로와 세로로 출력'''
        result = char * a
        for i in range(a):
            print(result)

a = int(input())
c = "helloworld "

hw = HelloWorld(c)

hw.helloCopy(a, c)
hw.helloCopy2(a)
hw.helloReverse()
hw.helloRectangle(a, c)
