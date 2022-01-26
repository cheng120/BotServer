from re import T
import string
import pymongo

class botReturn:
    bot_key = "my_bot_key"
    bot_returns = "my_bot_returns"
    def __init__(self) -> None:
        self.myclient  = pymongo.MongoClient("mongodb://localhost:27017/")
        self.my_db = self.myclient[self.bot_key]
        self.my_col = self.my_db[self.bot_returns]
        pass
    
    
    def checkMsg(self,msg,re_msg):
        where = {'keyword':msg,'returns':re_msg}
        res = self.my_col.find(where)
        if res is not None:     
            for i in res:
                return i
        else:
            return None
    
    def addMsg(self,msg,re_msg):
        # 添加信息 
        # 添加之前验证是否已经存在如果已经存在更新
        bot_msg = self.checkMsg(msg,re_msg)
        print(bot_msg)
        if bot_msg is None:
            msg_dict = {"keyword":msg,"returns":re_msg}
            res = self.my_col.insert_one(msg_dict)
            if res:
                return True
            else:
                return False
        else:
            return True
    
    # 暂时不用更新
    # def updateMsg(self):
    #     pass
    
    # 获取消息
    def getMsg(self,msg):
        # 根据msg 查询并随机返回一个回复
        where = {'$sample':{'size':1}}
        match = {'$match':{"keyword":msg}}
        res = self.my_col.aggregate([match,where])
        print([match,where])
        for i in res: 
            return i['returns']
