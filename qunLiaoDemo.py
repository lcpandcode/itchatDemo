# -*- coding: UTF-8 -*-
#群聊自动回复demo
# 加载库
from itchat.content import *
import requests
import json
import itchat
itchat.auto_login(hotReload = True)
# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer
# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
    print name

    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']
# 注册文本消息，绑定到text_reply处理函数


# 现在微信加了好多群，并不想对所有的群都进行设置微信机器人，只针对想要设置的群进行微信机器人，可进行如下设置
@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
    item = group_id(u'过过过！') # 根demo据自己的需求设置
    print msg['FromUserName']
    if msg['FromUserName'] == '@11432fd6aacd8741a1afb4f8f5262c8bf86bb32979b41a5898061f536000be6c' :
        print msg['ToUserName']
        itchat.send(u'%s' % tuling(msg['Text']), item)
itchat.run()

