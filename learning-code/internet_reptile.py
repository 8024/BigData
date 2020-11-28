import urllib.request as urllib2
from http import cookiejar

url = "http://www.baidu.com"

response = urllib2.urlopen(url)
print(response.getcode())
print(len(response.read()))

request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response = urllib2.urlopen(request)
print(response.getcode())
print(len(response.read()))

cj = cookiejar.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print(response.getcode())
print(cj)
print(len(response.read()))
