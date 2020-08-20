import requests, json

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream=True)
print(r.text)
#print(r.json()) <-- error occur
print(r.encoding) # None 으로 나옴

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    b = json.loads(line) # dict
    """
    print(type(b))
    print(b['origin'])
    """
    for e in b.keys():
        print("key: {}, value: {}".format(e, b[e]))


s.close()
