'''
    枚举:描述类型
    
'''


from enum import Enum

class VIP(Enum):
    YELLOW=1
    # YELLOW=2
    GREEN=1
    BLACK=3

# for x in VIP:
#     print(x)
print(VIP.GREEN)#此时  YELLOW 和 GREEN  的值相等  会输出YELLOW，会把GREEN看做YELLOW别名
# print(type(VIP.YELLOW.value))

# print(type(VIP.YELLOW.name))
# print(type(VIP.YELLOW))
# print(VIP['YELLOW'])
# print(type(VIP['YELLOW']))
# VIP.YELLOW=10


#普通类 的变量可以的更改，python 没有真正的常量
class Common():
    YELLOW=1

