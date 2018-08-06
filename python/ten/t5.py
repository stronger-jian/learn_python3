'''
https://blog.csdn.net/mrzhoug/article/details/51585615
'''
import re
a='Python & C# pHp C# C# C#'

def convert(value):
    # print(value)
    matched=value.group()#得到具体数字
    return '!!!'+matched


r= re.sub('C#',convert,a)
# a=a.replace('C#','go')
print(r)

