from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return redirect(url_for("home"))

@app.route("/home",methods=["GET","POST"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
