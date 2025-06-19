import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib
import base64
import os

# Load the model using joblib
model = joblib.load('stacking_custom.joblib')

# Load the model's expected columns (model_columns)
with open('model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

# Wind direction angle mapping
wind_direction_angle = {
    'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5, 'E': 90, 'ESE': 112.5,
    'SE': 135, 'SSE': 157.5, 'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5,
    'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
}

# List of all possible locations (dummy variables)
locations = [
    'Adelaide', 'Albany', 'Albury', 'AliceSprings', 'BadgerysCreek', 'Ballarat',
    'Bendigo', 'Brisbane', 'Cairns', 'Canberra', 'Cobar', 'CoffsHarbour', 'Dartmoor',
    'Darwin', 'GoldCoast', 'Hobart', 'Katherine', 'Launceston', 'Melbourne', 
    'MelbourneAirport', 'Mildura', 'Moree', 'MountGambier', 'MountGinini', 'Newcastle', 
    'Nhil', 'NorahHead', 'NorfolkIsland', 'Nuriootpa', 'PearceRAAF', 'Penrith', 'Perth', 
    'PerthAirport', 'Portland', 'Richmond', 'Sale', 'SalmonGums', 'Sydney', 'SydneyAirport', 
    'Townsville', 'Tuggeranong', 'Uluru', 'WaggaWagga', 'Walpole', 'Watsonia', 'Williamtown', 
    'Witchcliffe', 'Wollongong', 'Woomera'
]

# Function to set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Function to preprocess input data and handle dummy variables
def preprocess_input(user_input):
    input_data = pd.DataFrame([user_input])

    for loc in locations:
        input_data[loc] = 1 if loc == user_input['Location'] else 0
    input_data = input_data.drop(columns=['Location'])

    for col in ['WindGustDir', 'WindDir9am', 'WindDir3pm']:
        angles = input_data[col].map(wind_direction_angle)
        input_data[col] = np.sin(np.radians(angles)) + np.cos(np.radians(angles))

    input_data['RainToday'] = 1 if user_input['RainToday'] == 'Yes' else 0
    input_data = input_data[model_columns]
    return input_data

# Function to make a prediction
def predict_weather(user_input):
    processed_input = preprocess_input(user_input)
    processed_input = pd.DataFrame(processed_input, columns=model_columns)
    prediction = model.predict(processed_input)
    return prediction

# Streamlit UI
st.title("Weather Prediction: Will it Rain Tomorrow?")

location = st.selectbox('Location', locations)
rain_today = st.selectbox('Rain Today', ['Yes', 'No'])
min_temp = st.number_input('Minimum Temperature (°C)', -50, 50, 18)
max_temp = st.number_input('Maximum Temperature (°C)', -50, 50, 25)
rainfall = st.number_input('Rainfall (mm)', 0.0, 500.0, 15.0)
wind_gust_dir = st.selectbox('Wind Gust Direction', wind_direction_angle.keys())
wind_gust_speed = st.number_input('Wind Gust Speed (km/h)', 0, 200, 25)
wind_dir_9am = st.selectbox('Wind Direction at 9am', wind_direction_angle.keys())
wind_dir_3pm = st.selectbox('Wind Direction at 3pm', wind_direction_angle.keys())
wind_speed_9am = st.number_input('Wind Speed at 9am (km/h)', 0, 200, 20)
wind_speed_3pm = st.number_input('Wind Speed at 3pm (km/h)', 0, 200, 30)
humidity_9am = st.number_input('Humidity at 9am (%)', 0, 100, 80)
humidity_3pm = st.number_input('Humidity at 3pm (%)', 0, 100, 75)
pressure_9am = st.number_input('Pressure at 9am (hPa)', 900, 1100, 1010)
pressure_3pm = st.number_input('Pressure at 3pm (hPa)', 900, 1100, 1008)
temp_9am = st.number_input('Temperature at 9am (°C)', -50, 50, 19)
temp_3pm = st.number_input('Temperature at 3pm (°C)', -50, 50, 22)

user_input = {
    'Location': location,
    'RainToday': rain_today,
    'MinTemp': min_temp,
    'MaxTemp': max_temp,
    'Rainfall': rainfall,
    'WindGustDir': wind_gust_dir,
    'WindGustSpeed': wind_gust_speed,
    'WindDir9am': wind_dir_9am,
    'WindDir3pm': wind_dir_3pm,
    'WindSpeed9am': wind_speed_9am,
    'WindSpeed3pm': wind_speed_3pm,
    'Humidity9am': humidity_9am,
    'Humidity3pm': humidity_3pm,
    'Pressure9am': pressure_9am,
    'Pressure3pm': pressure_3pm,
    'Temp9am': temp_9am,
    'Temp3pm': temp_3pm
}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

rain_img = os.path.join(BASE_DIR, "image", "rain_day.jpg")
sunny_img = os.path.join(BASE_DIR, "image", "sunny_day.jpg")


# Predict and show result with background
if st.button('Predict'):
    prediction = predict_weather(user_input)
    
    if prediction == 1:
        set_background(rain_img)
        st.success("🌧️ It will rain tomorrow!")
    else:
        set_background(sunny_img)
        st.success("☀️ It will not rain tomorrow!")

