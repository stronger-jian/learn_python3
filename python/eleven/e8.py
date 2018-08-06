def curve_pre():
    a=25 #环境变量
    def curve(x):
        # print('this is a function')
        return a*x*x
    return curve 


def curve_pre1():
    a=30 #环境变量
    def curve(x):
        # print('this is a function')
        return a*x*x
    return curve 
a=10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(10))

