import urllib.request
import time
for i in range(60):
    url = 'https://surlfs.f5.si'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    time.sleep(60)

   