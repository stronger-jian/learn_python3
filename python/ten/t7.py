import re
a= '8c621d23S3297'

r=re.match('\d',a)
print(r)#<re.Match object; span=(0, 1), match='8'>
print(r.group())#8
r1=re.search('\D',a)
print(r1.span())
r2=re.findall('\d',a)
print(r2)