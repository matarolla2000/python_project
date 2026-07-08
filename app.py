from flask import Flask, render_template

app = Flask(__name__)

#key = ""
#url = "http://weatherapi.com"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/forecast", methods=["post"])
def forecast():
    return render_template("forecast.html")

@app.route("/contact")
def contact():
    pass

app.run(debug=True)