class Student():
        #一个班级学生人数
    sum=0


    '''
    https://blog.csdn.net/qq_37616069/article/details/79386966
        __init__方法 没有返回：
使用方式：
def 类名:
        #初始化函数，用来完成一些默认的设定
        def __init__():
            pass


     总结：
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形	参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
    '''
    def __init__(self,name1,age):
        self.name=name1
        self.age=age
        self.__score=0
        # print(Student.sum1)
        
        # print(name)#形参name
        # print('gouzao')
   

    def marking(self,score):
        if score<0:
            print('成绩不能小于0')
        else:
            self.__score=score
            print(self.name+'同学的成绩是'+str(self.__score))

    def do_homework(self):
        # self.__class__.sum1+=1
        # print('当前学生总人数:'+str(self.__class__.sum1))
        print('homework')

'''
    并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
'''
    @classmethod#可以通过类和实例来调用
    def plus_sum(cls):
        cls.sum+=1
        # print(Student.name)
        print(cls.sum)
        
    @staticmethod    #经常有一些跟类有关系的功能但在运行时又不需要实例和类参与的情况下需要用到静态方法
    def add(x,y):
        print(Student.sum)
        # print(name)
        print('this is a static method ')

# student1=Student()
student2=Student('ook',20)
student3=Student('li',20)
student2.marking(99)
student2.__score=-1
print(student3._Student__score)#Python不允许实例化的类访问私有数据,但可以_className__attrName 访问属性
# print(student2.__dict__)
# print(student3.__dict__)
# print(student3.__score)
# print(student2.__dict__)
# student2.marking(1)
student2.plus_sum()
Student.plus_sum() 
# student2.add(1,2)
# Student.add(1,2)
# student2.plus_sum()
# student2.plus_sum()
# student2.plus_sum()
# Student.plus_sum()
# student3=Student('li',20)
# Student.plus_sum()
# student4=Student('hao',20)
# Student.plus_sum()
# print(student2.__dict__)
# print(Student.__dict__)