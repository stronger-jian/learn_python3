from enum import Enum

class VIP(Enum):
    YELLOW=1
    YELLOW_alias=1
    GREEN=2
    BLACK=3

a=1
print(VIP(a))