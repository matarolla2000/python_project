from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forecast", methods=['post'])
def forecast():
    return render_template("forecast.html", forecast="")

@app.route("/get_forecast", methods=['post'])
def get_forecast():
    city = request.form['city']
    key = "5c302aef56104659ba671146260606"
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return render_template("forecast.html", forecast="Такого города не найдено.")
    forecast = f"Прогноз погоды для {city}: \n Температура: {data['current']['temp_c']}°C"
    return render_template("forecast.html", forecast=forecast)

@app.route("/contact", methods=['post'])
def contact():
    return render_template("contact.html")

app.run(debug=True)