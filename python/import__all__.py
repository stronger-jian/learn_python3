
#import test.test1.c6   这种引用方法 会提示c6不存在
'''
    c6 中的__all__决定的是 * 
    __all__=['a','c']  此时没有 b
    from test.test1.c6 import *    会找不到b
    from test.test1.c6 import b    会打印出b
'''
from test.test1.c6 import *

print(b)