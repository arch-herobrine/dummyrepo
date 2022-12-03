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
    url5 = 'https://archmusicbot-3.arch-herobrine.repl.co'
    req5 = urllib.request.Request(url5)
    with urllib.request.urlopen(req5) as res5:
        body5 = res5.read()
    url6 = 'https://archmusicbot-4.arch-herobrine.repl.co'
    req6 = urllib.request.Request(url6)
    with urllib.request.urlopen(req6) as res6:
        body6 = res6.read()
    url7 = 'https://qawsedrftgyhujikolp.arch-herobrine.repl.co'
    req7 = urllib.request.Request(url7)
    with urllib.request.urlopen(req7) as res7:
        body7 = res7.read()
    time.sleep(60)

   
