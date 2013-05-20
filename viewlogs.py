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


import urllib2


def xordec(ctext, key):
    rtntxt = ''
    loopcnt = 0
    keycnt = 0
    while loopcnt < len(ctext)/2:
        rtntxt = rtntxt + chr(int(ctext[loopcnt*2:loopcnt*2+2], 16) ^ ord(key[keycnt]))
        loopcnt += 1
        keycnt += 1
        if keycnt > len(key)-1:
            keycnt = 0
    return rtntxt


logname = raw_input('What is the name of the logfile you want to view?\n[?] ')

try:
    response = urllib2.urlopen('http://www.yoursite.com/' + logname)
    result = response.read()
except:
    print '[!] There was an error getting the data! :\'('
    exit(0)

ids = []
nids = []

for line in result.split('\n'):
    if line[:5] == '*[ID]':
        ids.append(line.replace('*', '').replace('[ID]', ''))
    if line[:6] == '*[NID]':
        nids.append(line.replace('*', '').replace('[NID]', ''))

print 'Valid starting ID\'s:'

vids = []

for idl in ids:
    if not idl in nids:
        vids.append(idl)

for vid in vids:
    print '[+] ' + vid

print ''

while True:
    selid = raw_input('What session do you want to view? (Leave blank to exit)\n[?] ')
    if selid == '':
        exit(0)
    selidkey = raw_input('What key did session "' + selid + '" use?\n[?] ')

    printnext = False
    recordnextline = False

    for line in result.split('\n'):
        if recordnextline:
            selid = line.replace('*', '').replace('[NID]', '')
            recordnextline = False
        if printnext:
            print xordec(line, selidkey)
            printnext = False
            recordnextline = True
        if line == '*[ID]' + selid + '*':
            printnext = True

# :)
