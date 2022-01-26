import re
class message :
    all_message = []
    CQ_type = [
        "face",
        "record",
        "video",
        "at",
        "share",
        "music",
        "reply",
        "forward",
        "xml",
        "json",
        "image",
        "redbag",
        "poke",
        "gift",
        "node",
        "cardimage",
        "tts",
    ]

    def __init__(self,message) -> None:
        self.all_message = message
        self.all_message['CQ_type'] = self.getCqType()
        self.all_message['message'] = self.getMessageBody()
        pass

    
    #获取信息类型 群聊/私聊 group/private
    def get_message_type(self):
        return self.all_message['message_type']


    #获取信息类型 群聊/私聊 group/private
    def get_self_id(self):
        return self.all_message['self_id']


    #获取群号/私聊qq号
    def get_number(self):
        if self.get_message_type() == 'group':
            return self.all_message['group_id']
        elif self.get_message_type() == 'private':
            return self.all_message['user_id']
        else:
            print('出错啦！找不到群号/QQ号')
            exit()
    # 获取信息发送者的QQ号
    def get_user_id(self):
        return self.all_message['user_id']

    #获取发送的信息
    def get_raw_message(self):
        return self.all_message['raw_message']

    #查找txt文本数据库
    def txt_msg(self,msg):
        fp = open("./bots/txt.txt", "w+",encoding='utf-8')
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
            if '[CQ:at,qq='+self.get_self_id()+'] ' + s1 == msg:
                fp.close()
                return s2


    #获取CQ信息type
    def getCqType(self):
        #获取CQ类型
        pattern = re.compile(r'(?<=:).*?(?=,)')
        method_type = pattern.search(str(self.all_message['message']))
        if method_type:
            #匹配出CQ消息类型
            if method_type.group() in self.CQ_type:
                return method_type.group()
            else:
                return False # 未知消息类型
        else:
            return False # 普通消息
        pass

    
    def getMessageBody(self):
        #获取CQ消息主题 字符串截取
        index = self.all_message['message'].find("]")
        message_body = self.all_message['message'][index+1:]
        if message_body:
            #匹配出CQ主题
            return message_body
        else:
            return self.all_message['message'] # 普通消息
        
    
    def getAtUserId(self):
        pattern = re.compile(r'(?<=qq=).*?(?=])')
        at_uid = pattern.search(str(self.all_message['raw_message']))
        if at_uid:
            #匹配出CQ消息类型
            return at_uid.group()
        else:
            return False # 未知消息类型
