import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from preprocessing import clean_text

# load dataset
df = pd.read_csv("data/spam.csv")

# rename columns if needed
df.columns = ['label', 'text']

# clean text
df['cleaned_text'] = df['text'].apply(clean_text)

# convert labels
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# features
X = df['cleaned_text']
y = df['label']

# vectorization
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# train model
model = MultinomialNB()

model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")

# save model
pickle.dump(model, open("models/model.pkl", "wb"))

# save vectorizer
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))