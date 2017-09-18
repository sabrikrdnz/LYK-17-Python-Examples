import json
def menu():
	f = open("yemekliste.txt","r")
	oku = f.read()
	menu = json.loads(oku)
	return menu
def siparis():
	#devam eeeettt