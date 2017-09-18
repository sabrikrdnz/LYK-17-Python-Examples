import requests
import json
 
x =requests.get('http://jsonplaceholder.typicode.com/posts/1')
content = x.content.decode('utf8').replace("'",'"')
js = json.loads(content)
for key,value in js:
	print(key,value)