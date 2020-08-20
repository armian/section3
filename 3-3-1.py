import requests, json

"""
r = requests.get('https://api.github.com/events')
# 문제가 생겼을 때, 예외상황을 발생시켜 줌
r.raise_for_status()
print(r.text)
"""
jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies')

"""
r = requests.get('http://httpbin.org/cookies', cookies=jar)
r.raise_for_status()
print(r.text)
"""

"""
r = requests.get('https://github.com', timeout=3)
print(r.text)
"""

# POST (여기서는 fake Rest 방식으로 운영)
"""
r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
print(r.text)
"""

payload1 = {'key1': 'value1', 'key2': 'value2'}      # dict
payload2 = (('key1', 'value1'), ('key2','value2'))   # tuple
payload3 = {'some':'nice'}

# dict payload 이용
r = requests.post('http://httpbin.org/post', data=payload1)  # form
print(r.text)

# tuple payload 이용
r = requests.post('http://httpbin.org/post', data=payload2)
print(r.text)

# json payload 이용
r = requests.post('http://httpbin.org/post', data=json.dumps(payload3)) # json
print(r.text)
