filter
list_x=[1,2,0,0,22,3,400,0]
list_u=['x','T','A','b','K']
r=filter(lambda x:x.isupper(),list_u)
print(list(r))