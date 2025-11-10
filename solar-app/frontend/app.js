const API_BASE = "http://51.20.142.29:5000";

const input = document.getElementById("cityInput");
const btn = document.getElementById("searchBtn");
const result = document.getElementById("result");
const cityName = document.getElementById("cityName");
const avgTemp = document.getElementById("avgTemp");
const cloud = document.getElementById("cloud");
const sun = document.getElementById("sun");
const energy = document.getElementById("energy");
const error = document.getElementById("error");

btn.addEventListener("click", async () => {
  const city = input.value.trim();
  if (!city) {
    error.textContent = "Please enter a city name.";
    return;
  }

  error.textContent = "Loading...";
  result.classList.add("hidden");

  try {
    const res = await fetch(`${API_BASE}/forecast?city=${encodeURIComponent(city)}`);
    if (!res.ok) throw new Error("City not found");
    const data = await res.json();

    cityName.textContent = data.city;
    avgTemp.textContent = data.tomorrow.avg_temp_c.toFixed(2);
    cloud.textContent = data.tomorrow.cloudcover_mean.toFixed(2);
    sun.textContent = data.tomorrow.sunshine_hours.toFixed(2);
    energy.textContent = data.prediction.toFixed(2);

    error.textContent = "";
    result.classList.remove("hidden");
  } catch (e) {
    error.textContent = "❌ " + e.message;
  }
});
