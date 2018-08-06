
import time

def decorator(func):#decorator 装饰
    def wrapper():#wrapper  封装
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print('this is a function')

f1()
# f=decorator(f1)
# f()