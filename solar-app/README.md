# Weather-Based Solar Forecast App. 

## Overview.

This is a simple Flask-based web application that predicts solar energy generation based on live weather data. 
Users can enter a city name, view real-time weather (temperature, sunlight and cloud cover). And check the predicted solar energy output for the next day using a trained AI model. 

 ## Features.
  - Live weather data from Open-meteo API
  - AI based solar energy forecast (Regression model)
  - Frontend dashboard built with HTML, CSS, and JavaScript
  - Flask REST API (/forecast?city=) returning JSON results
  - Ready for deployment on AWS EC2 (backend) and S3 (frontend)

  ## Folder structure

      solar-forecast-app/
    │
    ├── app.py                 # Flask backend
    ├── model_train.py         # Train regression model
    ├── model.pkl              # Saved trained model
    ├── requirements.txt       # Python dependencies
    │
    └── frontend/              # Web interface
        ├── index.html
        ├── app.js
        └── style.css

  ## How to run Locally
  
  ### 1. Clone the repo:
  git clone https://github.com/ThiliC/solar-forecast-app.git
cd solar-forecast-app
 
  ### 2. Create a virtual environment and install dependencies:
  pip install -r requirements.txt

  ### 3. Run the Flask app:
  python app.py

  ### 4. Open the browser:
  Backend: http://127.0.0.1:5000
  Frontend: open frontend/index.html (or run with Live Server)

## Author
**Thilini Cooray**
Business Information Technology | Haaga-Helia UAS
AI-Powered Renewable Energy Forecast Project






[def]: i