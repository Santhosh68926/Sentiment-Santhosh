# -*- coding: utf-8 -*-
"""sentiment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ig5uDYCQs9AkK7NwuSns-f1h5vOsi0Bw
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

text = "I love this product. It's amazing!"

sentiment_scores = sia.polarity_scores(text)

if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")
print(f"Positive Score: {sentiment_scores['pos']}")
print(f"Negative Score: {sentiment_scores['neg']}")
print(f"Neutral Score: {sentiment_scores['neu']}") 
print(f"Compound Score: {sentiment_scores['compound']}")
