'''
    多层条件判断语句

'''

a=input()
print(type(a))
print('a is'+a)
a=int(a)   #此时 输入 True 和 '1' 都会报错  ：invalid literal for int()
if a==1:
    print('pingguo')
else:
    if a==2:
        print('xiangjiao')
    else:
        if a==3:
            print('orange')
        else:
            print('shopping')