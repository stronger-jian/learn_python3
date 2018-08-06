'''
    序列化
'''


import json

student=[
    {"name":"jian","age":18,"flag":False},
    {"name":"jian","age":18}
]
json_str=json.dumps(student)
print(json_str)
print(type(json_str))