import re
from flask import Flask, request
from plugin.botData import botReturn

from plugin.dice import Dice

'''注意，这里的import api是另一个py文件，下文会提及'''
import api

app = Flask(__name__)

'''监听端口，获取QQ信息'''


@app.route('/', methods=["POST","GET"])
def post_data():
    #  路由
    # 下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式
    req = request.get_json()
    if req.get("meta_event_type") == "heartbeat":
        return "alive"
    else:
        #记录CQ信息
        Api = api.Api(request.get_json())    
        Api.route(request.get_json())  # 将 Q号和原始信息传到我们的后台
    return "end"



@app.route('/test', methods=["POST","GET"])
def test():
    msg = request.args.get('msg', '')
    re_msg = request.args.get('re_msg', '')
    print("测试功能")
    bot = botReturn()
    res = bot.getMsg(msg)
    print(res)
    return res['returns']


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9999)  # 此处的 host和 port对应上面 yml文件的设置
