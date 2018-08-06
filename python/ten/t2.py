import re
a='pythonpythonpythonpython'

r=re.findall('(python){3}',a)
print(r)
