
day=6
def get_sunday():
    return 'sunday'

def get_firstday():
    return 'firstday'

def get_friday():
    return 'friday'

def get_unknow():
    return 'Unknow'

week={
    0:get_sunday,
    1:get_friday,
    2:get_firstday
}
day_name=week.get(day,get_unknow)()
print(day_name)