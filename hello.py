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

@app.route("/doc_org/")
def doc_org():
	return render_template("doc_org.html")

@app.route("/doc_editor/")
def doc_editor():
	return render_template("doc_editor.html")

@app.route("/doc_signer/")
def doc_signer():
	return render_template("doc_signer.html")

@app.route("/login/")
def login():
	return render_template("login.html")

@app.route("/check_status/")
def check_status():
	return render_template("check_status.html")


if __name__ == "__main__":
    app.run()