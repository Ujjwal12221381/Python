# multi-level

class A:
    def Ainfo(self):
        print("A")

class B(A):
    def Binfo(self):
        print("B")
        A().info()

class C(B):
    def Cinfo(self):
        print("C")
        B().info()
        
Cobj=C()
Cobj.Cinfo()