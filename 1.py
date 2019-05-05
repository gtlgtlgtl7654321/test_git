from urllib import request

req = request.Request('http://www.douban.com')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
with request.urlopen('https://www.douban.com') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    print('Data:',data.decode('utf-8'))