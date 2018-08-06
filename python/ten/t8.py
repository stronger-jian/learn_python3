import re
a= 'life is short, i use python,i love python'

r=re.search('life(.*)python(.*)python',a)
# r=re.findall('life(.*)python',a)
print(r.group(0,1,2))
# print(r.group(1))
# print(r.group(2))
# print(r)
print(r.groups())