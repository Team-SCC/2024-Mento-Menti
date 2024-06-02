class HelloWorld:
    def __init__(self, string):
        self.string = string
    
    def helloCopy(self, num: int):
        '''
        @param int num: 매개변수
        '''
        result = self.string * num
        print(result)
    
    def helloCopy2(self, num: int):
        '''
        @param int num: 매개변수
        '''
        for i in range(num):
            print(self.string)
    
    def helloReverse(self):
        print("dlrowolleh")
    
    def helloRectangle(self, num:int):
        '''
        @param int num: 매개변수
        '''
        for i in range(num):
            result = self.string * num
            print(result)


if __name__ == "__main__":
    hw = HelloWorld("hello")
    hw.helloCopy(5)
    hw.helloCopy2(5)
    hw.helloReverse()
    hw.helloRectangle(5)