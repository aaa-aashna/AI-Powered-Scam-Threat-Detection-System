import re
import nltk
from nltk.corpus import stopwords

# download stopwords
nltk.download('stopwords')

# load english stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):

    # convert to lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # split text into words
    words = text.split()

    # remove stopwords
    words = [word for word in words if word not in stop_words]

    # join cleaned words
    return " ".join(words)