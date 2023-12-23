class A:
    answer=42
    def __init__(self):
        self.answer=21
        self.__add__=lambda x,y:x.answer+y
    def __add__(self,y):
        return self.answer-y
    
print(A()+5)

#16
#class variable is over rided by instance variable
