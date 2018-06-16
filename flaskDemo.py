# -*- coding: UTF-8 -*-
from flask import *
import thread
app = Flask(__name__,static_path='/static')

@app.route('/')
def hello_word():
    return "hello"

import itchat
def login():
   itchat.auto_login()
   #返回二维码给前端
   itchat.run()
   return "登录成功!"

@app.route('/login')
def do_login():
    #线程执行后台微信相应程序
    thread.start_new_thread(login(),())
    return "yes"
if __name__=='__main__':
    app.run()