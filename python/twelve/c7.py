
import time


def f1():
    print('this is a function')

def f2():
    print('this is a function')

def get_current_time(func):
    print(time.time())
    func()

get_current_time(f1)
get_current_time(f2)