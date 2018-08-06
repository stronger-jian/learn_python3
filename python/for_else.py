'''
    python 中的 for  else  存在陷阱
    https://www.cnblogs.com/dspace/p/6622799.html
'''

a=[['apple','banana','orange'],(1,2,3)]
for x in a:
    # if 'apple' in x:
    #     break
    for y in x:
       if y == 'apple':
            # break
            print(y,end=' | ')
else:
    print('fruit is gone')
# a=[1,2,3]
# for x in a:
#     if x == 2:
#         continue
#     print(x)
# else:
#     print('hello')