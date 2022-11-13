import urllib.request
import time
for i in range(60):
    url = 'https://surlfs.f5.si'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        
    url2 = "https://authbot-on-TH.arch-herobrine.repl.co"
    with urllib.request.urlopen(req2) as res2:
        body2 = res2.read()
    time.sleep(60)

   
