origin=0
global origin
def go(step):
    # global origin
    new_pos=origin+step
    # origin=0
    origin+=step
    return origin

print(go(2))
print(go(3))
print(go(1))

