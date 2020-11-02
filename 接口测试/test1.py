import requests

base_url = 'http://test.bms.zhisland.com/cms/feed/dynamic/publish'


# url参数
param = {
}
# bosy参数
form_data = {
    "feedType":"2",
    "publisherUser":"6161466868050690055",
    "recommend":False,
    "circleIds":"",
    "startTime":1603962290534,
    "endTime":1635498290534,
    "content":"啦啦啦啦111"
}

# 请求头
header = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'165',
    'Content-Type':'application/json;charset=UTF-8',
    'Cookie':'_test_m_uid=6691956257210761223; _test_m_auth=_WOly1c7CA-10COl-hxJXtRefZL_phqeznE8FRITWw**; _pre_m_uid=6692257215035736068; _pre_m_auth=_WagzlI-DQ-21yal-hxJXd9efJL7pBicy3E5EhAXUA**; sid=7cf62399-6463-4b51-b168-3eea103400dc',
    'Host':'test.bms.zhisland.com',
    # 'Origin': 'http://test.bms.zhisland.com',
    'Pragma':'no-cache',
    # 'Referer':'http://test.bms.zhisland.com/cms/feed/dynamic/publishAdd',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}

# cookies信息
cookie = {
    'test_m_uid':'6691956257210761223',
    '_test_m_auth':'_WOly1c7CA-10COl-hxJXtRefZL_phqeznE8FRITWw**', 
    '_pre_m_uid':'6692257215035736068',
    '_pre_m_auth':'_WagzlI-DQ-21yal-hxJXd9efJL7pBicy3E5EhAXUA**',
    'sid':'7cf62399-6463-4b51-b168-3eea103400dc',
}

# get请求传递参数
# r_response = requests.get(base_url,params=param,headers=header,cookies=cookie)
# 传递信息为 form格式
# r_response = requests.post(base_url,data=form_data,headers=header,cookies=cookie)
# 如果form传递得是json格式
# r_response = requests.post(base_url,data=form_data,headers=header,cookies=cookie)

# 传递信息为json格式
r_response = requests.post(base_url,json=form_data,headers=header,cookies=cookie,timeout=0.00001)


print(r_response.url)
print(r_response.status_code)   # 状态码
print(r_response.headers)   #响应头 
print(r_response.text)  # 相应内容
print(r_response.json())    # 将响应内容以json格式返回




