# AI-Powered Scam Threat Detection System

An NLP-based Machine Learning system designed to detect scam and phishing-related messages using text preprocessing, feature extraction, and classification techniques.

The project combines concepts from cybersecurity and machine learning to identify potentially malicious SMS messages or text content and classify them as either **Scam** or **Legitimate**.

---

# Features

* Text preprocessing pipeline
* Stopword removal using NLTK
* TF-IDF vectorization
* Machine Learning-based classification
* Scam vs Legitimate message prediction
* Modular project structure
* Model saving and loading support

---

# Tech Stack

## Languages

* Python

## Libraries & Tools

* Scikit-learn
* Pandas
* NumPy
* NLTK
* Jupyter Notebook
* Pickle

---

# Project Structure

```bash
ai-threat-detection-system/
│
├── app/
├── data/
│   └── spam.csv
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── eda.ipynb
├── README.md
├── requirements.txt
```

---

# Dataset

The project uses publicly available spam/phishing message datasets containing SMS and text-based scam samples.

Example dataset format:

| label | text                                   |
| ----- | -------------------------------------- |
| spam  | Congratulations! You won a free iPhone |
| ham   | Hey, are we meeting today?             |

Approximate dataset size:

* 50,000+ text samples

---

# Machine Learning Pipeline

## 1. Text Preprocessing

The preprocessing stage includes:

* Lowercasing
* Removing special characters
* Tokenization
* Stopword removal

## 2. Feature Extraction

TF-IDF Vectorization is used to convert textual data into numerical features suitable for machine learning models.

## 3. Model Training

The project uses:

* Multinomial Naive Bayes Classifier

## 4. Prediction

The trained model predicts whether a given message is:

* Scam
* Legitimate

---

# Model Performance

| Metric   | Score |
| -------- | ----- |
| Accuracy | ~91%  |
| F1 Score | ~0.89 |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Powered-Scam-Threat-Detection-System.git
```

Move into the project directory:

```bash
cd AI-Powered-Scam-Threat-Detection-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run the Project

## Train the model

```bash
python src/train_model.py
```

## Run prediction

```bash
python src/predict.py
```

Enter a sample message:

```bash
Congratulations! You won a free vacation package.
```

Example Output:

```bash
Scam Message
```

---

# Future Improvements

* Deep Learning-based NLP models
* Real-time phishing URL detection
* Email scam analysis
* Web application deployment
* Transformer/LLM integration
* Multi-language scam detection

---

# Applications

* Cybersecurity systems
* Spam filtering
* Fraud prevention
* Threat intelligence systems
* Intelligent communication security

#
