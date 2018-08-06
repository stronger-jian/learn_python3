#元组比较特殊

students={
    'aaa':11,
    'bbb':23,
    'ccc':32
}

b=(key for key,value in students.items())
# print(b)
for x in b:
    print(x)