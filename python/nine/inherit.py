'''
https://www.cnblogs.com/z941030/p/4851650.html
在python中继承中的一些特点：

1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。使用super().__init__()或parentClassName.__init__()
2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

'''


from a3 import Human
class Student(Human):  
    # sum=0

    #一个班级学生人数
    def __init__(self,school,name,age):
        self.school=school
        # Human.__init__(self,name,age)
        super(Student,self).__init__(name,age)
        # self.__score=0

    def do_homework(self):
        super(Student,self).do_homework()
        print('homework')

student1=Student('东华小学','小明',19)
student1.do_homework()
# print(student1.name)
# print(student1.age)
# Student.do_homework('')
