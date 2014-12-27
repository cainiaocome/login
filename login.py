#!/usr/bin/python

import httplib,urllib2,hashlib
import time

username = '1120122078'
password = '661230'
def md5(mate):
	m = hashlib.md5()
	m.update(mate)
	return m.hexdigest()
def prepare():
	hc = httplib.HTTPConnection(host = '10.0.0.55')
	return hc

def main():
    i = 0;
    hc = prepare()
    password1 = md5(password)
    password2 = password1[8:24]
    data = "username="+username+"&password="+password2+"&drop="+"0"+"&type=1&n=100"
    headers = {"Content-type":"application/x-www-form-urlencoded",
        'connection':'keep-alive',
        "Accept":"text/plain"}
    try:
        hc.request(method = 'POST',url = '/cgi-bin/do_login',body = data,headers = headers)
        response = hc.getresponse()
    except: 
        print 'exception not handled, please contact the author'
    result = response.read()
    if result == 'username_error':
        print 'username wrong'
    elif result == 'password_error':
        print 'password wrong'
    else:
        print 'login ok'
        while True:
            data = 'uid={}'.format(result);
            hc.request(method = 'POST',url = '/cgi-bin/keeplive',body = data,headers = headers)
            response = hc.getresponse()
            print response.read()
            time.sleep(1)
            i = i +1;
            if i>5:
                break;
	return 0

if __name__ == '__main__':
	main()
