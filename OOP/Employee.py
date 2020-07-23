"""class Employee:
    def __init__(self,name1,id1,branch1):
        self.name=name1
        self.id=id1
        self.branch=branch1
    def fullname(self):
        print("Hello, BATHULA PRATHAP")


emp_1=Employee('Prathap','R151331','CSE')
emp_2=Employee('Naveen','R151298','CSE')
print(emp_1)
print(emp_2)

print(emp_1.id)
print(emp_2.id)

emp_1.fullname()"""


"""class A:
    a='This is first'
    
x=A()
y=A()

print(x.a)
print(y.a)
print(A.a)
A.a='This is second'
print(A.a)
print(y.a)
print(x.a)"""



"""class Foo(object):

    variable = 1

    def method(self, param):
        print("run instance method (%s,%s)"  %(self,param))

    @classmethod
    def class_method1(cls, param):
        print ("run class method (%s,%s)" % (cls, param))

    @classmethod
    def class_method2(cls):
        print (cls.variable)

    @staticmethod
    def static_method1(param):
        print ("run static method (%s)" % param)

    @staticmethod
    def static_method2():
        print (Foo.variable)

foo = Foo()

foo.method("instance method")
#Foo.method("instance method again")

foo.class_method1("class method 1")
foo.class_method2()
Foo.class_method1("class method 1 again")
Foo.class_method2()

foo.static_method1("static method 1")
foo.static_method2()
Foo.static_method1("static method 1 again")
Foo.static_method2()"""

"""class Employee:
    
    raise_int=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@email.com'
        self.pay=pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=self.pay*self.raise_int
        

class Developer(Employee):
    raise_int=1.10
    
    def __init__(self,first,last,pay,pro_language):
        super().__init__(first,last,pay)
        self.pro_language=pro_language
    
class Manager(Employee):
    
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees= employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees :
            print('--> ',emp.fullname())
    
emp_1=Developer('Prathap','Bathula',20000,'python')
emp_2=Developer('Naveen','Cinnappa',30000,'java')
mng_1=Manager('Daya','Paravatha',50000,[emp_1])

mng_1.add_emp(emp_2)
print(mng_1.print_emp())
print(mng_1.first)

#print(emp_1.pro_language)
#print(emp_1.fullname())
#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)"""

"""class Sample:
    
    def __init__(self,a):
        self.__a=a
    def get_a(self):
        return self.__a
    def set_a(self,a):
        self.__a=a
        
sam=Sample(5)
print(sam.get_a())
sam.set_a(3)
print(sam.get_a())"""

class Employee:
     
    def __init__(self,first,last):
         self.first=first
         self.last=last
         
    """@property
    def email(self):
        return "{}.{}@email.com".format(self.first,self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last"""
    
    def __repr__(self):
        return '{} {}'.format(self.first,self.last)
    
    def __str__(self):
        return'{}-{}'.format(self.first,self.last)
    
    
        
emp_1=Employee('prathap','bathula')
print(emp_1)
#print(emp_1.fullname)
#emp_1.fullname='ganga prathap'
#print(emp_1.email)

