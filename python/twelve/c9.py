'''
多个实参，放到一个元组里面,以*开头，可以传多个参数；**是形参中按照关键字传值把多余的传值以字典的方式呈现
'''

import time

def decorator(func):#decorator 装饰
    def wrapper(*args,**kw):#wrapper  封装
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(fun_num1):
    print('this is a function'+fun_num1)

f1('nihao')

@decorator
def f2(fun_num1,fun_num2):
    print('this is a function'+fun_num1)
    print('this is a function'+fun_num2)

@decorator
def f3(fun_num1,fun_num2,**kw):
    print('this is a function'+fun_num1)
    print('this is a function'+fun_num2)
    print(kw)
# f=decorator(f1)
# f()
# f2('hello','world')
f3('hello','world',a=1,b='w',c=2)