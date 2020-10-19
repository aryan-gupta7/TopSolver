from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    return redirect(url_for("home"))


@app.route("/home")
def home():
    return render_template("home.html", home="active", solution="passive", faqs="passive", about="passive")


@app.route("/solutions")
def solution():
    return render_template('solution.html', home="passive", solution="active", faqs="passive", about="passive")


@app.route("/about")
def about():
    return render_template('about.html', home="passive", solution="passive", faqs="passive", about="active")


@app.route("/FAQs")
def faqs():
    return render_template("faqs.html", home="passive", solution="passive", faqs="active", about="passive")


if __name__ == "__main__":
    app.run(debug=True)
