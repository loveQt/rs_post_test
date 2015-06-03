# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import re
import requests
from bs4 import BeautifulSoup
import xlwt
import time

def Login():
    login_url = 'http://rs.xidian.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
    loginpage = urllib.urlopen('http://rs.xidian.edu.cn/member.php?mod=logging&action=login').read()
    login_soup = BeautifulSoup(loginpage)
    formhash_tag = login_soup.find('input',attrs={'name':'formhash'})
    formhash = formhash_tag['value']
    print formhash
    params = {
            "answer":"",
            #"formhash":formhash,
            #"loginfield":"username",
            #"loginsubmit":"",
            "password":'*****',
            "questionid":"0",
            "referer":"http://rs.xidian.edu.cn/",
            "username":'*****',
            }
    jar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(jar)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    req = urllib2.Request(login_url)
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Connection','keep-alive')
    req.add_header('User-Agent',"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0")
    req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    #req.add_header('Accept-Encoding','gzip, deflate')
    #req.add_header('Referer',"http://rs.xidian.edu.cn/forum.php")
    enparams = urllib.urlencode(params)
    page = urllib2.urlopen(req,enparams)
    print page
    data = page.read()
    #print data
    global g_cookie
    global g_formhash
    g_cookie = page.info()['set-cookie']
    t_cookie = re.sub(r'poK_formhash=deleted','',g_cookie)
    r_formhash = re.search(r"poK_formhash=[^;]+",t_cookie)
    #if r_formhash:
        #g_formhash = re.sub(r'poK_formhash=','',r_formhash.group())
    #return
    murl = 'http://rs.xidian.edu.cn/forum.php?mod=viewthread&tid=722705&extra=page%3D1'
    treq = urllib2.Request(murl)
    treq.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    treq.add_header('Connection','keep-alive')
    treq.add_header('User-Agent',"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0")
    treq.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3') 
    tpage = urllib2.urlopen(treq)
    print tpage
    tdata = tpage.read()
    login_soup = BeautifulSoup(tdata)
    formhash_tag = login_soup.find('input',attrs={'name':'formhash'})
    formhash = formhash_tag['value']
    print formhash
    #print tdata
    
    murl = 'http://rs.xidian.edu.cn/forum.php?mod=post&action=reply&fid=72&tid='+'750469'+'&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
    treq = urllib2.Request(murl)
    treq.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    treq.add_header('Connection','keep-alive')
    treq.add_header('User-Agent',"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0")
    treq.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3') 
    '''
    postdata = {
        'formhash': formhash,
        'message':'路过帮顶了~~~',
        #posttime    1433250379
        'subject':'',	
        'usesig':'1'
        }
    '''
    postdata = 'message=%E8%B7%AF%E8%BF%87%E5%B8%AE%E9%A1%B6%E4%BA%86%7E%7E%7E&posttime=1433250379&formhash='+formhash+'&usesig=1&subject=++'
    tpage = urllib2.urlopen(treq,postdata)
    print tpage
    tdata = tpage.read().decode('utf-8')
    print tdata
    
    
    '''
    for num in range(1,2):
        #http://rs.xidian.edu.cn/bt.php?mod=browse&c=1005&page=
        murl = 'http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=72&page='+str(num)
        treq = urllib2.Request(murl)
        treq.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        treq.add_header('Connection','keep-alive')
        treq.add_header('User-Agent',"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0")
        treq.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')    
        try:
            tpage = urllib2.urlopen(treq,enparams)
        except:
            time.sleep(2)
            tpage = urllib2.urlopen(treq,enparams)
        print tpage
        tdata = tpage.read().decode('utf-8')
        #print tdata
        #mod=viewthread&amp;tid=749781&amp;extra=page
        movie = r'<strong> .*?</strong> ]</span>..<span class="tps">&nbsp;...<a href="forum.php\?mod=viewthread&tid=([_0-9_]{6})'
        #movie = r'tid=([_0-9_]{0,6})\&extra=page'
        mlist = re.findall(movie,tdata,re.S)
        for each in mlist:
            print each
            #http://rs.xidian.edu.cn/forum.php?mod=post&action=reply&fid=72&tid=749278&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1
            posturl = 'http://rs.xidian.edu.cn/forum.php?mod=post&action=reply&fid=72&tid='+each+'&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
       '''     
'''
750582
750580
750469
734909
749278
750523
742144
745212
747578
727625
745113
737785
738164
714338
722705
749820
'''
Login()
