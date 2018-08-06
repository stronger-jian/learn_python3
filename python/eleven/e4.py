from enum import Enum

class VIP(Enum):
    YELLOW=1
    YELLOW_alias=1
    # RED=1
    GREEN=2
    BLACK=3

for x in VIP.__members__.items():
    print(x)

for x in VIP.__members__:
    print(x)


# print(VIP.RED)