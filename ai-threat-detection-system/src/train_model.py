import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("data/spam.csv")

X = df["message"]
y = df["label"]

model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(X, y)

joblib.dump(model, "models/model.pkl")

print("Model trained successfully")