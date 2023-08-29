from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/city", methods=['GET', 'POST'])
def search_city():
    data = {}
    if request.method == 'POST':
        city = request.form['cityName']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
        response = requests.get(url).json()
        if response.get('cod') != 200:
            message = response.get('message', '')
            return render_template("index.html", message=message)
        coord = response.get('coord',{})  # Get location's informations
        if coord:
            data['lon'] = coord['lon']
            data['lat'] = coord['lat']
        main_data = response.get('main', {}) #retrieve data such as temp, weather...
        if main_data:
            data['temp'] = main_data['temp']
            data['temp_min'] = main_data['temp_min']
            data['temp_max'] = main_data['temp_max']
        return render_template("index.html", data=data)


if __name__== "__main__":
    app.run(debug=True)