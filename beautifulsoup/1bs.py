#imdb top250 filmi BeautifulSoup kütüphanesi ile çekme.
import requests
from bs4 import BeautifulSoup

html_data =requests.get("http://www.imdb.com/chart/top?ref_=nv_wl_img_3").content

soup_data= BeautifulSoup(html_data, "html.parser")

tbody_data = soup_data.find("tbody",{"class":"lister-list"})

for tr_data in tbody_data.find_all("tr"):
 	isim_td = tr_data.find("td",{"class":"titleColumn"})
 	rating_td = tr_data.find("td",{"class":"ratingColumn"})
 	print(isim_td.find("a").text,rating_td.find("strong").text)