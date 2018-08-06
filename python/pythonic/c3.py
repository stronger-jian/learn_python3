#列表推导式
#list  set  dict tuple

a={1,2,3,4,5,6,7,8,9,10}

b={i**2 for i in a if i>=5}
print(b)