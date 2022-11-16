import urllib.request
import time
for i in range(60):
    url = 'https://surlfs.f5.si'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        
    url2 = "https://archmusicbot-1.arch-herobrine.repl.co"
    req2 = urllib.request.Request(url2)
    with urllib.request.urlopen(req2) as res2:
        body2 = res2.read()
        
    url3 = 'https://surlfs-mk2.f5.si'
    req3 = urllib.request.Request(url3)
    with urllib.request.urlopen(req3) as res3:
        body3 = res3.read()

    url4 = 'https://archmusicbot-2.arch-herobrine.repl.co'
    req4 = urllib.request.Request(url4)
    with urllib.request.urlopen(req4) as res4:
        body4 = res4.read()
    url4 = 'https://archmusicbot-3.arch-herobrine.repl.co'
    req4 = urllib.request.Request(url4)
    with urllib.request.urlopen(req4) as res4:
        body4 = res4.read()
    url4 = 'https://archmusicbot-4.arch-herobrine.repl.co'
    req4 = urllib.request.Request(url4)
    with urllib.request.urlopen(req4) as res4:
        body4 = res4.read()
    time.sleep(60)

   
