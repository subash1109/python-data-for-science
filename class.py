
class Person ():


    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.ms=False

    def print_(self):
        print('name :',self.name)
        print('age  :',self.age)
        print('ms   :',self.ms)
    def up_age(self)  :
         self.age=self.age+1
    def up_ms(self,a):
        self.ms=a



a=Person('django',45)
a.up_age()
a.up_ms(True)

a.print_()
