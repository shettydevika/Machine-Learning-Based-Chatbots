import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pandas as pd

# Load data
data = pd.read_csv('data.csv')
X = data['query']
y = data['response']

# Create a pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X, y)

# Save the model
import joblib
joblib.dump(model, 'chatbot_model.pkl')
