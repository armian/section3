import requests

s = requests.Session()

# PUT(FETCH), DELETE, GET, POST
#r = s.get('https://www.naver.com')
#print('1', r.text)

r = s.get('http://httpbin.org/cookies', cookies={'from':'myName'})
print('2', r.text)

url = 'http://httpbin.org/get'
headers = {'user-agent' : 'myPythonApp_1.0.0'}

r = s.get(url, headers=headers)
print('3', r.text)

s.close()

# with 문을 사용하여 작성
with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)
