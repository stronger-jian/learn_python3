list_x=[1,2,3,4,5]
list_y=[1,2,3,4,5,6,7,8,9]
def square(x):
    return x*x
#r的长度  取决于  list_x和list_y的最小长度

r=map(lambda x,y:x*x+y ,list_x, list_y)
print(list(r))