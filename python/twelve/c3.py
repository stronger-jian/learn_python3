#map  适用于对循环/迭代的操作
# map()函数接收两个参数，一个是函数，一个是序列

list_x=[1,2,3,4,5,6,7,8,9]
# list_y=[]
def square(x):
    return x*x

r=map(square,list_x)
print(r)
print(list(r))
# for x in list_x:
#     r=square(x)
#     list_y.append(r)

# print(list_y)