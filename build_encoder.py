import joblib
from sklearn.preprocessing import LabelEncoder

# ✅ STEP 1: Define all weather-related labels
weather_labels = [
    'Clear', 'Clouds', 'Rain', 'Snow', 'Mist', 'Haze',
    'Fog', 'Drizzle', 'Smoke', 'Thunderstorm'
]

# ✅ STEP 2: Fit the encoder with these labels
encoder = LabelEncoder()
encoder.fit(weather_labels)

# ✅ STEP 3: Save the encoder to 'encoder.pkl'
joblib.dump(encoder, 'encoder.pkl')

print("✅ encoder.pkl rebuilt with labels:", encoder.classes_)