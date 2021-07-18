import requests
url = 'http://192.168.1.7:6969/api/gg-search'
data = {'data': 'học bách khoa tphcm thì chỗ ăn chỗ ở thế nào'}
data = 'học bách khoa tphcm thì chỗ ăn chỗ ở thế nào'
r = requests.post(url = url,data=data.encode('utf-8'))
print(r)