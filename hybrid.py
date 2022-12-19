class A:
    def About(self):
        print(" A class")
    def Ainfo(self):
        print("A")

class B(A):
    def Binfo(self):
        print("B")
        A().About()

class C(A):
    def Cinfo(self):
        print("C")
        A().Ainfo()
class D(B,C):
    def Dinfo(self):
        print("C")
        B().Binfo()
        C().Cinfo()

Dobj=D()
Dobj.Dinfo()