'''
    reduce 适用于连续运算
'''
from functools import reduce

list_x=['1','2','3','4','5']

r=reduce(lambda x,y:x+y,list_x,'a')
print(r)
#((((1+2)+3)+4)+5)

