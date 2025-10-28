import joblib
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load("model.pkl")

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city):
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    r = requests.get(GEOCODE_URL, params=params, timeout=15)
    data = r.json()
    if not data.get("results"):
        return None
    top = data["results"][0]
    return top

def get_weather(lat, lon, timezone):
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": timezone,
        "current": "temperature_2m,cloud_cover",
        "daily": "temperature_2m_max,temperature_2m_min,cloud_cover_mean,sunshine_duration",
        "forecast_days": 2
    }
    r = requests.get(FORECAST_URL, params=params, timeout=20)
    data = r.json()

    # tomorrow = index 1
    tmax = data["daily"]["temperature_2m_max"][1]
    tmin = data["daily"]["temperature_2m_min"][1]
    cloud_mean = data["daily"]["cloud_cover_mean"][1]
    sun = data["daily"]["sunshine_duration"][1] / 3600  # convert to hours
    avg_temp = (tmax + tmin) / 2

    pred = float(model.predict([[avg_temp, cloud_mean, sun]])[0])

    return {
        "current": data["current"],
        "tomorrow": {
            "avg_temp_c": avg_temp,
            "cloudcover_mean": cloud_mean,
            "sunshine_hours": sun
        },
        "prediction": round(pred, 2)
    }

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/forecast")
def forecast():
    city = request.args.get("city", "")
    loc = geocode_city(city)
    if not loc:
        return jsonify({"error": "City not found"}), 404
    lat, lon, tz = loc["latitude"], loc["longitude"], loc["timezone"]
    result = get_weather(lat, lon, tz)
    return jsonify({"city": city, **result})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
