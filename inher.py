
class par1():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def print_(self):
        print('i m from par1 ')
        print('a =',self.a)
        print('b =',self.b)

class par2():
    def __init__(self,a,b):
        self.c=a
        self.d=b

    def print__(self):
        print('i m from par2 ')
        print('c =',self.c)
        print('d =',self.d)

class child_ (par1,par2):
    def __init__(self):
        par1.__init__(self,4,5)
        par2.__init__(self,6,8)
        self.print_()
        self.print__()

c=child_()
