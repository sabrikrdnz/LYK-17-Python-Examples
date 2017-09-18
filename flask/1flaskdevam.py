from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	isimler = ["Ahmet", "Burak", "Ayşe", "Kıvırcık"]
	return render_template("1index.html",isimlistesi=isimler)

@app.route("/secondpage")
def second_page():
	return "Second Page"

#app.run(debug=True, host="0.0.0.0", port=5000)
app.run(debug=True)