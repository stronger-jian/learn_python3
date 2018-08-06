import re
a= 'A8c621d23S3297'

def covert(value):
    matched=value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r=re.sub('\d',covert,a)
print(r)

# re.match()
