class Oint():

    def __init__(self):
        self.i = 0

    def add(self, a,b):
        self.i = a+b
        return self.i

    def sub(self, a, b):
        self.i = a-b
        return self.i

    def set(self, a):
        self.i = a
        return self.i