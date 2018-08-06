
# for x in range(10,0,-1):
#     print(x,end='|')
a=[1,2,3,4,5,6,7]
# for x in range(0,len(a),2):    #-->1|3|5|7|  正序
for x in range(len(a)-1,-1,-2):   #-->7|5|3|1|  倒序
    print(a[x],end='|')    
# b=a[0:len(a):2]   #2 表示步长  就是隔几个取出来  这种方法 比较pythonic
# print(b)   #此时 end='|'  这种样式  不会起作用  [1, 3, 5, 7]|
