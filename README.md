### Financial Sentiment Analysis

This repository contains two approaches for financial sentiment analysis on text data:

TF-IDF + Logistic Regression – a classical machine learning approach

FinBERT – a transformer-based model pretrained on financial texts

Overview

Financial sentiment analysis is the task of classifying financial text (headlines, news, reports) into positive, negative, or neutral sentiments. This project demonstrates both:

The advantages and limitations of traditional ML models on small datasets

How domain-specific transformers like FinBERT handle financial language more effectively

Dataset

Financial PhraseBank

CSV format: label,text

Labels:

0 - Negative

1 - Neutral

2 - Positive

Note: The small dataset causes the Logistic Regression model to be biased toward neutral sentences.
