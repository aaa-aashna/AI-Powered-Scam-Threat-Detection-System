import pickle

from preprocessing import clean_text

# load model
model = pickle.load(open("models/model.pkl", "rb"))

# load vectorizer
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def predict_message(message):

    cleaned = clean_text(message)

    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)

    if prediction[0] == 1:
        return "Scam Message"
    else:
        return "Legitimate Message"


# test
msg = input("Enter message: ")

print(predict_message(msg))