import urllib.request
import time
true = True
while True:
    url = 'https://surlfs.f5.si'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()


    url2 = 'https://surlfs-mk2.f5.si'
    req2 = urllib.request.Request(url2)
    with urllib.request.urlopen(req2) as res2:
        body2 = res2.read()
    time.sleep(60)
