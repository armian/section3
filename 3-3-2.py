import requests, json

# RestAPI : POST, GET, PUT(UPDATE, REPLACE) (FETCH : UPDATE, MODIFY), DELETE

payload1 = {'key1': 'value1', 'key2': 'value2'}      # dict
payload2 = (('key1', 'value1'), ('key2','value2'))   # tuple
payload3 = {'some':'nice'}

"""
# PUT이지만 POST와 동일하게 동작함
r = requests.put('http://httpbin.org/put', data=payload1)
print(r.text)
"""

"""
r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=payload1)
r.raise_for_status()
print(r.text)
"""

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
r.raise_for_status()
print(r.text)
