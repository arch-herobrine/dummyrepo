import urllib.request

url = 'https://example.com/api/v1/resource'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read()

urll = 'https://example.com/api/v1/resource'

reqq = urllib.request.Request(urll)
with urllib.request.urlopen(reqq) as res:
    bodyy = res.read()