from flask import Flask, render_template, request

app = Flask(__name__)

#key = ""
#url = "http://weatherapi.com"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/forecast", methods=['post'])
def forecast():
    return render_template("forecast.html", forecast="")

@app.route("/get_forecast", methods=['post'])
def get_forecast():
    city = request.form['city']
    forecast = f"Прогноз погоды для {city}"
    return render_template("forecast.html", forecast=forecast)

@app.route("/contact", methods=['post'])
def contact():
    return render_template("contact.html")

app.run(debug=True)