# -*- coding: UTF-8 -*-
import itchat
import thread
def login():
    print "login begin"
    itchat.auto_login()
    itchat.run()
    print "login end"
print ('begin')
thread.start_new_thread(login,())
print ('end')
while 1 :
    pass