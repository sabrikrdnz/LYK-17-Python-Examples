#Bir dosyadan sözlük okuyalım ama okuduğumuz sözlük string olmalı.
#Sonra bunu sözlüğe çevir, key ve value ları bastır anacım.
import json
oku = open("module4json.txt","r")
okun = oku.readline()
js = json.loads(okun)
print(js)
print(type(js))