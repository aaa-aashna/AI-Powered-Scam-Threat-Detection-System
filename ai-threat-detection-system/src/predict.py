import joblib

model = joblib.load("models/model.pkl")

def predict_message(text):
    prediction = model.predict([text])

    if prediction[0] == 1:
        return "Scam"
    return "Safe"