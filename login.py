#!/usr/bin/python

import httplib,urllib2,hashlib
import requests
import time

username = 'webadmin'
password = '888888'
def md5(mate):
	m = hashlib.md5()
	m.update(mate)
	return m.hexdigest()

def main():
    i = 0;
    headers = {"Content-type":"application/x-www-form-urlencoded",
        'connection':'keep-alive',
        "Accept":"text/plain"}
    payload = {'action':'login',
            'username':'webadmin',
            'password':'888888',
            'ac_id':'8',
            'type':'1',
            'wbaredirect':'',
            'mac':'',
            'user_ip':''}
    r = requests.post(url='http://10.0.0.55/cgi-bin/srun_portal', data=payload, headers=headers);
    print r.text
    #if result == 'username_error':
    #    print 'username wrong'
    #elif result == 'password_error':
    #    print 'password wrong'
    #else:
    #    print result
    #    print 'login ok'
    #    while True:
    #        data = 'uid={}'.format(result);
    #        hc.request(method = 'POST',url = '/cgi-bin/keeplive',body = data,headers = headers)
    #        response = hc.getresponse()
    #        print response.read()
    #        time.sleep(1)
    #        i = i +1;
    #        #if i>5:
    #        #    break;
	#return 0

if __name__ == '__main__':
	main()
