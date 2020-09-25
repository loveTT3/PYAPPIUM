import csv
import requests
import time


# 获取手机号
def csv_phone():
    with open(r'C:\Users\user\Desktop\我叔的手机号.csv',mode='r',encoding='utf-8') as f:
        readf = csv.reader(f)
        for i in readf:
            if i:
                print(i[0])
                return i[0]


urldata={

}

#消息头
header1 = {
'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Content-Length': '35',
'Content-Type': 'application/json;charset=UTF-8',
'Cookie':'ARK_ID=JS9b93b51c6cd9e0365ab60f44cf9631599b93; \
        _test_m_uid=6323818023257899012;\
        _test_m_auth=_WOlyFQ4Cwix1Cal-hlCXNVac5D4ohqayX4zHRAQWg**; \
        sid=291af193-c5f4-4538-a4de-24d93c71c397',
'Host': 'test.bms.zhisland.com',
'Origin': 'http://test.bms.zhisland.com',
'Pragma': 'no-cache',
'Referer': 'http://test.bms.zhisland.com/circle/index',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


#消息体
data={
"feedType":2,
    "publisherUser":"6161466868050690055",
    "content":"这个是内容呢\n好长好长",
    "recommend":False,
    "startTime":1590566427339,
    "endTime":1622102427339
}
json1 = {
    "circleId":735,
    "memberUids":"137"
    }

cookie = {
    'ARK_ID':'JS9b93b51c6cd9e0365ab60f44cf9631599b93',
    '_test_m_uid':'6323818023257899012',
    '_test_m_auth':'_WOlyFQ4Cwix1Cal-hlCXNVac5D4ohqayX4zHRAQWg**',
    'sid':'291af193-c5f4-4538-a4de-24d93c71c397'
}

# url =  'http://test.bms.zhisland.com/cms/feed/dynamic/publish'
# url1 = 'https://test.www.zhisland.com/bms-api-app/user/login/password'
url2 = 'http://test.bms.zhisland.com/cms/bizcircle/member/batch/add'
def gogo():
    r = requests.post(url2,headers=header1,json=json1,cookies= cookie)
    print('响应码： ',r.status_code)
    print(r.headers)
    print(r.text,type(r.text))
    # print(r.text['msg'])

gogo()