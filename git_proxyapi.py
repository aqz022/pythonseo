import requests

url = "http://api.xxx.cn/VAdb=1"#代理接口
html = requests.get(url,timeout=30)
ip = html.text.strip()
proxyHost = ip[:ip.index(':')]
proxyPort = ip[ip.index(':'):].strip(':')

print (proxyHost)
print (proxyPort)
