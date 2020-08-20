import requests

# Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code)
print(r.ok)
"""
if r.ok == True:
    if r.status_code == 200
"""

# https://jsonplaceholder.typicode.com

#r = s.get("https://jsonplaceholder.typicode.com/albums")
r = s.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.text)
print(r.json())
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content)
print(r.raw)
s.close()
