from flask import Flask, render_template

app = Flask(__name__)

kullanicilar = {"kivircik":"kasid","ok":"samsung","sabri":"karadeniz"}

@app.route("/")
def hello():
	isimler = ["Ahmet", "Burak", "Ayşe", "Kıvırcık"]
	return render_template("2kullanici.html",isimlistesi=isimler)


@app.route("/kullanici/<kullanici>")
def kullanicilar_goruntuleme(kullanici):

	if kullanicilar.get(kullanici,None):
		bulunan_kullanici = kullanicilar.get(kullanici)
	else:
		bulunan_kullanici = None
	return render_template("kullanici.html",bulunan=bulunan_kullanici,
							kullanici_url=kullanici)


@app.route("/secondpage")
def second_page():
	return "Second Page"

#app.run(debug=True, host="0.0.0.0", port=5000)
app.run(debug=True)