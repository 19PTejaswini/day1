'''
import calendar
class dob():
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year
    def display1(self):
        print(self.date)
        print(calendar.month_name[self.month])
        print(self.year)
class details(dob):
    def __init__(self,name,age,date,month,year) -> None:
        self.name = name
        self.age = age
        self.date = date
        self.month = month
        self.year = year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)

ob = details("Ram",25,24,8,2001)
ob.display()
ob.display1()
'''
'''
class vehicle:
    def __init__(self,fuel) -> None:
        self.fuel = fuel
    def display1(self):
        print(self.fuel)

class motor(vehicle):
    def __init__(self,cc,fuel) -> None:
        self.fuel = fuel
        self.cc = cc
        super().__init__(fuel)
    def display2(self):
        print(self.cc)
        print(self.fuel)

class car(motor):
    def __init__(self,name,cc,fuel) -> None:
        self.name = name
        self.fuel = fuel
        self.cc = cc
        super().__init__(cc,fuel)
    def display3(self):
        print(self.name)
        print(self.cc)
        print(self.fuel)

ob = car("BMW","300cc","Petrol")
ob.display1()
ob.display2()
ob.display3()
'''
'''
from abc import  abstractclass
@abstractclass
class shape:
    def __init__(self) -> None:
        pass
    def area(self,):
        pass
class rectangle(shape):
    def __init__(self) -> None:
        pass
    def area(self,l,b):
        return l*b
class square(shape):
    def __init__(self) -> None:
        pass
    def area(self,s):
        return s*s
r = rectangle()
s = square()
print(s.area(10))
print(r.area(10,30))
'''

try:
    a = 10//0
except Exception as e : 
    print(e)
else:
    print(a)
finally:
    print('finally block')