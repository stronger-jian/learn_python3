def f1():
    a=10
    def f2():
        # a=28
        # return a 
        a*20
    #     print(a)
    # print(a)
    return f2
    # print(a)
f=f1()
print(f)
print(f.__closure__)