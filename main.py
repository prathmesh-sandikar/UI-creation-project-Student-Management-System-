from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Login():
 return render_template("Login.html")
@app.route("/register")
def collect_data():
 return render_template("Register.html")
@app.route("/search")
def Search():
 return render_template("Search.html")
@app.route("/delete")
def Delete():
 return render_template("Delete.html")
if __name__ == "__main__":
 app.run()
