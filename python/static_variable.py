'''
    静态变量  一般用大写表示
'''

ACOUNT='qiyue'
PASSWORD='123455'

print('please input acount')
user_accout=input()
print('please input password')
user_password=input()

if ACOUNT==user_accout and PASSWORD==user_password:
    print('success')
else:
    print('fail')


