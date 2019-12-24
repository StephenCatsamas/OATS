from builtIn import *


class pair():

    def __init__(self):
        self.i = Oint()

        self.j = Oint()

    def make(self, a, b):
        self.i = a

        self.j = b

        return (self)

    @staticmethod
    def add(self, a, b):
        self.i = Oint.add(a.i, b.i)

        self.j = Oint.add(a.j, b.j)

        return (self)


p = pair()
t = pair()

p.make(1, 9)
t.make(5, 7)

p.add(p,t)

print(p.i)
print(p.j)
