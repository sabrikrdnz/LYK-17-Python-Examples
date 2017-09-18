from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"

@app.route("secondpage")
def second_page():
	return "Second Page"

app.run(debug=True, host="0.0.0.0", port=5000)