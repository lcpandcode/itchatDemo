# -*- coding: UTF-8 -*-
import itchat
itchat.auto_login()
rooms = itchat.get_friends()
for i in rooms :
    print i['City']




