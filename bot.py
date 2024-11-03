import requests
import json
from time import sleep, strftime, localtime
from os import system
var = 1
erc = 0

geturl = "https://chat-go.jwzhd.com/open-apis/v1/bot/messages"
getpayload = {"token": "1f192788d0c14c339ffc8c21aadfd8be","chat-id": "992758867","chat-type": "group","before": "1"}
keywords1 = 'content":{"text":"/清屏"}'
keywords2 = 'commandName":"发送消息'
keywords3 = 'content":{"text":"/114514"}'
keywords4 = '/停止'
keywords41 = '"senderId":"6528966"'
keywords5 = '机器人骂人'
keywords6 = '"commandName":"设置群看板"'
keywords7 = '/取消看板'

posturl = "https://chat-go.jwzhd.com/open-apis/v1/bot/send?token=1f192788d0c14c339ffc8c21aadfd8be"
posturl2 = "https://chat-go.jwzhd.com/open-apis/v1/bot/board?token=1f192788d0c14c339ffc8c21aadfd8be"
posturl3 = "https://chat-go.jwzhd.com/open-apis/v1/bot/board-dismiss?token=1f192788d0c14c339ffc8c21aadfd8be"

headers = {
  'Content-Type': 'application/json; charset=utf-8'
}

time = strftime("%Y-%m-%d %H:%M:%S", localtime())
print(time," 程序初始化完成")

while var == 1 :
    get = requests.get(geturl, headers=headers, params=getpayload)
    
    if (keywords1 in get.text) :
        sendmsg = '''清屏






































清屏'''
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group",
            "contentType": "text",
            "content": {
                "text": sendmsg
            }
        })
        requests.post(posturl, headers=headers, data=postpayload)
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        print(time," 检测到清屏指令，已发送指定消息")
    if (keywords2 in get.text) :
        start = get.text.find('content":{"text":')
        stop = get.text.find('sendTime')
        sendmsg = get.text[start+18:stop-4]
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group",
            "contentType": "markdown",
            "content": {
                "text": sendmsg
            }
        })
        requests.post(posturl, headers=headers, data=postpayload)
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        print(time," 使用指令“/发送消息”发送了一条消息：",sendmsg)
    if (keywords3 in get.text) :
        while erc < 13 :
            if erc == 0 :
                sendmsg = "1"
            if erc == 2 :
                sendmsg = "4"
            if erc == 3 :
                sendmsg = "5"
            if erc == 4 :
                sendmsg = "1"
            if erc == 5 :
                sendmsg = "4"
            if erc == 6 :
                sendmsg = "1"
            if erc == 7 :
                sendmsg = "9"
            if erc == 8 :
                sendmsg = "1"
            if erc == 9 :
                sendmsg = "9"
            if erc == 10 :
                sendmsg = "8"
            if erc == 11 :
                sendmsg = "1"
            if erc == 12 :
                sendmsg = "0"

            postpayload = json.dumps({
                "recvId": "992758867",
                "recvType": "group",
                "contentType": "text",
                "content": {
                    "text": sendmsg
                }
            })
            requests.post(posturl, headers=headers, data=postpayload)
            erc = erc + 1
        erc = 0
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        print(time,' 使用指令“/114514”发送了"1145141919810"')
    if (keywords4 in get.text) :
        if (keywords41 in get.text) :
            sendmsg = "已关闭"
            postpayload = json.dumps({
                "recvId": "992758867",
                "recvType": "group",
                "contentType": "text",
                "content": {
                    "text": sendmsg
                }
            })
            requests.post(posturl, headers=headers, data=postpayload)
            system('taskkill /f /im py.exe')
        sendmsg = "仅开发者可用"
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group",
            "contentType": "text",
            "content": {
                "text": sendmsg
            }
        })
        requests.post(posturl, headers=headers, data=postpayload)
    if keywords5 in get.text :
        sendmsg = "![](https://tc.d3tt.com/images/FiLLyMqGAD8Pl7lCtKqzWuh6jjLU.jpg)"
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group",
            "contentType": "markdown",
            "content": {
                "text": sendmsg
            }
        })
        requests.post(posturl, headers=headers, data=postpayload)
    if keywords6 in get.text :
        start = get.text.find('content":{"text":')
        stop = get.text.find('sendTime')
        sendmsg = get.text[start+18:stop-4]
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group",
            "contentType": "markdown",
            "content": sendmsg
        })
        requests.post(posturl2, headers=headers, data=postpayload)
        sendmsg2 = "992758867"
        postpayload = json.dumps({
            "recvId": "356286347",
            "recvType": "group",
            "contentType": "text",
            "content": {
                "text": sendmsg2
            }
        })
        requests.post(posturl, headers=headers, data=postpayload)
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        print(time,' 设置了群看板：',sendmsg)
    if keywords7 in get.text :
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group"
        })
        requests.post(posturl3, headers=headers, data=postpayload)
        postpayload = json.dumps({
            "recvId": "992758867",
            "recvType": "group",
            "contentType": "text",
            "content": {
                "text": "取消成功！"
            }
        })
        requests.post(posturl, headers=headers, data=postpayload)
        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        print(time,' 取消了该机器人群看板')
        
    sleep(5)

system('pause')
