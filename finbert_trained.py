from transformers import pipeline

# Load FinBERT model (CPU)
finbert = pipeline(
    "sentiment-analysis",
    model="yiyanghkust/finbert-tone",
    device=-1  # CPU
)

# Function to predict sentiment
def predict_financial_sentiment(text):
    result = finbert(text)[0]
    print(f"Input: {text}")
    print(f"Predicted Sentiment: {result['label']} (score={result['score']:.2f})")

# Example usage: take input from user
user_input = input("Enter a financial sentence to analyze sentiment: ")
predict_financial_sentiment(user_input)

