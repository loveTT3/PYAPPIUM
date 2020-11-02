import  requests



r = requests.get('http://test.bms.zhisland.com/cms/feed/dynamic')
print(type(r.cookies))
print(r.cookies)
for key,value in r.cookies.items():
    print(key + ":" + value)