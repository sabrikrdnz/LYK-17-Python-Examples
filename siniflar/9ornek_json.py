import requests
import json

 
x =requests.get('http://jsonplaceholder.typicode.com/users')
content = x.content.decode('utf8').replace("'",'"')
js = json.loads(content)

class User:
	user_list = []
	def __init__(self,id,name,username,email,phone,website):
		self.id=id
		self.name=name
		self.username=username
		self.email = email
		self.phone =phone
		self.website =website
		User.user_list.append(self)

for user in js:
	print("=====")
	print(user["username"])
	user = User(user["id"], user["name"], user["username"], user["email"], user["phone"], user["website"]) 
	print(User.user_list)