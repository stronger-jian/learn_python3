'''
反序列化 json-->python

'''

import json

json_str='[{"name":"jian","age":18,"flag":false},{"name":"jian","age":18}]'
note=json.loads(json_str)
print(note)
print(type(note))
print(note[0])
print(note[1])
# print(note['name'])