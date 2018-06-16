# -*- coding: UTF-8 -*-
value = 1
def test1() :
    global value
    value = value + 1
import pythonDemo1
content = dir(pythonDemo1)
print content
print __name__
print __file__
print __doc__
print __package__