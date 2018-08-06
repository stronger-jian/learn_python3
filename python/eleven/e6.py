from enum import Enum
from enum import IntEnum,unique

@unique#去重复
class VIP(IntEnum):
    YELLOW=1
    YELLOW_alias=10
    GREEN=2
    BLACK=3

