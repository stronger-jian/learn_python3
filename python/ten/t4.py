#概括字符集
#\d [0-9]
#\D [^0-9]
import re
qq='100000001'

r=re.findall('000$',qq)
print(r)