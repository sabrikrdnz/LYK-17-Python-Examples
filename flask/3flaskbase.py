from flask import Flask, render_template, request, redirect

app = Flask(__name__)

kullanicilar = {"kivircik":"kasid","ok":"samsung","sabri":"karadeniz"}
json_file = "kisiler.json"


@app.route("/kullanicilar")
def hello():
	return render_template("4kullanici_kaydi.html")

@app.route("/kaydet", method="POST")
def kaydet():
	try:
		kisilistesi = json.load(open(json_file,"r"))
	except Exception as e:
		kisilistesi = []
	
	if request.method == "POST":
		if request.form.get('isim',None) and request.form.get('telefon',None):
			kisilistesi.append({"isim":request.form.get('isim'),
								"telefon": request.form.get('telefon')})
			open(json_file,"w+").write(json.dumps(kisilistesi))
	return redirect("/kullanicilar")

#app.run(debug=True, host="0.0.0.0", port=5000)
app.run(debug=True)