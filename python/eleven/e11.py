origin=0
def address(pos):
    # # x=0
    # i=1
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos#这个地方必须有  必须改变
        return new_pos
    # x+=how_many
    # return x 
    return go
f=address(origin)
print(origin)
print(f(3))
print(f.__closure__[0].cell_contents)
print(f(5))
print(f.__closure__[0].cell_contents)
print(f(6))
print(f.__closure__[0].cell_contents)