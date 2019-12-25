from builtIn import *


class pair():

    def __init__(self):
        self.i = INT()

        self.j = INT()

    def make(self, a, b):
        self.i = a
        self.j = b

        return (self)


    def add(self, a, b):
        self.i = INT().add(a.i, b.i)

        self.j = INT().add(a.j, b.j)

        return (self)


p = pair()
t = pair()

p.make(1, 9)
t.make(5, 7)

p.add(p,t)

print(p.i)
print(p.j)


def func(a):
    print(a)

__main__.func(4)