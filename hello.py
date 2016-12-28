from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/create/")
def create():
	return render_template("secondpage.html")

@app.route("/review/")
def review():
	return render_template("review.html")

if __name__ == "__main__":
    app.run()