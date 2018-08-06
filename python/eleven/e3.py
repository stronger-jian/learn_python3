

from enum import Enum

class VIP(Enum):
    YELLOW=1
    GREEN=2
    BLACK=3


class VIP1(Enum):
    YELLOW=1
    GREEN=2
    BLACK=3
# result= VIP.GREEN > VIP.BLACK  
#枚举可以遍历，枚举和枚举之间可以进行'==','is'比较，但不可以进行大小比较
result= VIP.GREEN == VIP1.GREEN

print(result)