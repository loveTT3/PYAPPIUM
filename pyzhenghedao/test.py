import requests
import time
urldata={

}

#消息头
header = {
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '167',
'Cookie': 'ARK_ID=JS4af69a7d34565c72eb875fe56e372dcc4af6; _test_m_uid=6161466868050690055; \
        _test_m_auth=_WOly1c7CAuy1yWl-htGXtldfZj8qRiaznAzFBAUXQ**; _aid=wx48db7cb6e5e15e78;\
        sid=134e3f59-6c4a-4188-b2a3-ae9249d6bf92'
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

stime = time.time()
json = {
    "feedType":"2",
    "publisherUser":"6161466868050690055",
    "content":f"这个是内容呢\n好长好长--{stime}",
    "recommend":False,
    "startTime":1590566427339,
    "endTime":1622102427339
}

url =  'http://test.bms.zhisland.com/cms/feed/dynamic/publish'


def main():
    r = requests.post(url,headers=header,json=json)
    print('响应码： ',r.status_code)
    # print(r.headers)
    print(r.text,type(r.text))
    # print(r.text['msg'])

    # if r.headers['msg'] == '成功':
    #     print('操作成功')
    # print(r.text)



# __name__ 脚本方式运行时，返回固定字符串  __main__
# 以导入模块执行时  就是本模块名字
# print(__name__)

# 当前脚本执行  会立马执行可执行语句
# 以导入模块执行时，不执行可执行语句
if __name__ == '__main__':
    main()