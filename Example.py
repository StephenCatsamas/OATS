class int:
    def __init__(self):
        self.i = int()
    
    def set(self,a):
        self.i = a
    
    def add(self,a,b):
        self.i = a + b

    def toBas(self):
        return self.i

MyInt = int()

MyInt.set(3)

print(MyInt.toBas())

MyInt.add(1,5)

print(MyInt.toBas())

