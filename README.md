
# 🌦️ Rain Prediction Web App using Stacked Model

This project is a machine learning web application that predicts whether it will rain tomorrow, based on historical weather data. The backend model is a custom stacking ensemble that combines multiple base learners to improve prediction accuracy.

## 🔧 Technologies Used

- Python 3
- Streamlit
- Pandas, NumPy
- Scikit-learn, Joblib, Pickle
- Matplotlib (optional for analysis)
- Custom background image rendering using CSS

## 💡 Features

- **Stacked Ensemble Model**: Combines the predictions of multiple models for better performance.
- **Web Interface**: Built using Streamlit for simplicity and interactivity.
- **Dynamic Background**: Displays a different background depending on prediction result.
- **Input Fields**: User-friendly interface for entering all required weather parameters.

## 📁 File Structure

```
├── dataset.zip               # This have raw dataset and imputed dataset
├── server.py                 # Main Streamlit app code
├── stacking_custom.joblib    # Trained stacked model
├── model_columns.pkl         # List of model features used for prediction
├── image/
│   ├── rain_day.jpg          # Background image for rain prediction
│   └── sunny_day.jpg         # Background image for no-rain prediction
└── README.md                 # This file
```

## 🧠 Model Details

The stacking model includes:

- Base learners: Multiple classification models
- Meta-learner: Combines the outputs of the base learners to produce a final prediction
- Trained using scikit-learn and saved using `joblib`

## 🚀 How to Run the App

1. Clone the repository.
2. Make sure the required packages are installed.
3. Ensure the model (`stacking_custom.joblib`) and the feature list (`model_columns.pkl`) are in the same directory.
4. Place background images inside an `image/` folder.
5. Run the app:

```bash
streamlit run server.py
```

## 🧾 Input Fields in Web App

- **Location** (Dropdown)
- **Rain Today** (Yes/No)
- **Min/Max Temperature**
- **Rainfall**
- **Wind Direction & Speed (Gust, 9am, 3pm)**
- **Humidity (9am & 3pm)**
- **Pressure (9am & 3pm)**
- **Temperature (9am & 3pm)**

## 🎨 Background Image Logic

- If the model predicts **Rain (1)**: `rain_day.jpg` will be set as background.
- If the model predicts **No Rain (0)**: `sunny_day.jpg` will be set as background.

---

## 📬 Contact

**Anil Kumar**  
MIS Executive | Aspiring Data Analyst | • Python • SQL • Power BI • Excel • Machine Learning  
📧 [ak26458624@gmail.com](mailto:ak26458624@gmail.com) | 
[LinkedIn](https://www.linkedin.com/in/anil-kumar-554561225/)


