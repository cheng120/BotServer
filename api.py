import json
import urllib.parse
import socket
import requests
import re
import random
import Cq_message

'下面这个函数用来判断信息开头的几个字是否为关键词'
'如果是关键词则触发对应功能，群号默认为空'

bot_host = 'http://127.0.0.1'
bot_port = ":5700"
api_map = {
    0: "/send_private_msg", # 私聊
    1: "/send_group_msg", # 群聊
    2: "/send_msg", # 发送消息
    3: "/delete_msg", # 撤回消息
}

class Api:
    self_message_info = {}
    def __init__(self,message_info) -> None:
        self.self_message_info = Cq_message.message(message_info)
        pass
    
    
    def route(self,message_info):
        if self.self_message_info.get_message_type == "private":
            self.training_message()
        #判断是否是@触发
        if self.self_message_info.all_message['CQ_type'] == "at" or self.self_message_info.all_message['user_id'] == 1010460162:
            '''映射关键字 分发方法'''
            params_str = self.self_message_info.all_message['message'].strip()
            params = params_str.split(" ")
            if params[0] == "setu":  # 你们懂的
                '''分割参数'''
                setu(self.self_message_info.all_message['group_id'], params[1:])
            if params[0] == 'help':  # 你们懂的
                help_interface(self.self_message_info.all_message['group_id'])
            if params[0] == '学习':  # 你们懂的
                training_message(self.self_message_info)
            if params[0] == 'test':  # 你们懂的
                test(self.self_message_info.all_message['user_id'])
            return 1
        else:
            return 1
    
    


    def send_private_msg(self,uid, message, group_id=0, auto_escape="false" ):
        url = bot_host+bot_port+api_map[0];
        param = {"user_id": uid, "group_id": group_id, "message": message, "auto_escape":auto_escape}
        requests.post(url=url, data=param)
        return


    def send_group_msg(self,group_id, message, auto_escape="false" ):
        url = bot_host+bot_port+api_map[1]
        param = {"group_id": group_id, "message": message, "auto_escape":auto_escape}
        requests.post(url=url, data=param)
        return


    '''撤回消息'''
    def delete_msg(self,message_id):
        url = bot_host+bot_port+api_map[2]
        param = {"message_id": message_id}
        requests.post(url=url, data=param)
        return


    def setu(self,gid, params):
        num = 1
        tag = []
        r18 = 0
        if params[0]:
            num = params[0]
        if len(params) > 1:
            tag = params[1].split(",")
        if len(params) > 2:
            r18 = params[2]
        param = {
            'num': num,
            'tag': tag,
            'r18': r18,
            "size": "original",
            "proxy": "i.pixiv.re"
        }
        print(param)
        url = 'https://api.lolicon.app/setu/v2'
        menu = requests.post(url=url, json=param)
        data = menu.json()['data']
        print(data)
        for item in data:
            setu_url = item['urls']['original']  # 对传回来的涩图网址进行数据提取
            requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid,r'[CQ:image,' r'file=' + str(setu_url) + r']'))
        return


    def test(self,uid):
        return self.send_private_msg(uid, self.self_message_info.all_message["group_id"])


    def txt_msg(self,msg):
        fp = open("./robot/.log", "r",encoding='utf-8')
        while 1:
            s = fp.readline()
            if not s:
                fp.close()
                if flag == 2:
                    return
                return error()
            s = s.strip('\n')
            s1 = s.split(' ')[0]
            s2 = s.split(' ')[1]
            if '[CQ:at,qq=×××××] ' + s1 == msg:
                fp.close()
                return s2


    #错误
    def error(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1',5700))
        rand = random.randint(1,4)
        number = self.self_message_info.get_number()
        if rand == 1:
            msg = "我听不懂你在说什么哦"
        elif rand == 2:
            msg = "我好笨，听不懂呜呜呜"
        elif rand == 3:
            msg = "啊？发生了什么"
        elif rand == 4:
            msg = "干啥呢干啥呢"
        payload = "GET /send_group_msg?group_id=" + str(number) + "&message=" + msg + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
        client.send(payload.encode("utf-8"))
        client.close()


    #帮助界面
    def help_interface(group_id):
        number = group_id
        payload = "GET /send_group_msg?group_id=" + str(number) + "&message=学习方式：%0a私聊rabbit酱，发送学习信息。%0a学习格式：%27学习%27%20%2b%20发送信息%20%2b%20回复信息，以空格分开%0a例：学习%20我爱你%20我也爱你" + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1',5700))
        client.send(payload.encode("utf-8"))
        client.close()

    def training_message(self):
        s = self.self_message_info.get_raw_message()
        if s.split(' ')[0] != '学习':
            return
        s2 = s.split(' ')[1]
        s3 = s.split(' ')[2]
        s = s2 + ' ' + s3
        fp = open("./bot/txt.txt", "a+",encoding='utf-8')
        fp.write('\n')
        fp.write(s)
        fp.close()
        client_to_conn()
    
    
    def client_to_conn(self):
        label = self.self_message_info.get_message_type()
        number = self.self_message_info.get_number()
        msg = self.self_message_info.get_raw_message()
        if flag == 0:
            msg = self.txt_msg(self.self_message_info.get_raw_message())
        if label == 'group':
            payload = "GET /send_group_msg?group_id=" + str(number) + "&message=" + msg + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
        elif label == 'private':
            payload = "GET /send_private_msg?user_id=" + str(number) + "&message=××××" + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1',5700))
        client.send(payload.encode("utf-8"))
        client.close()



