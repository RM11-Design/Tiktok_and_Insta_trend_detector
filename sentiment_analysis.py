import csv
import pandas as pd
import nltk
from datetime import date 
# from transformers import pipeline
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os


# summarisation=pipeline("summarization",model="t5-small",framework="pt")

# This only works when a CSV file is uploaded from the frontend.

def read_comments(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df


# def sentiment_summary(df):
#     all_comments = df['Comments'].astype(str).str.cat(sep=' ')
#     summary = summarisation(all_comments,
#                             max_length=500,
#                             min_length=40,
#                             do_sample=False)
#     summarised_text = summary[0]['summary_text']
#     return summarised_text
     
# Assigned a variable which will be used for analysis.     
     
# # Sentiment_analysis 

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores['pos'] > 0 else 0    
    return sentiment

def overall_sentiment(df):
    df["Processed"] = df["Comments"].apply(preprocess_text)
    df["sentiment"] = df["Processed"].apply(get_sentiment)

    # This counts the number of unique values, so the number of 1s and 0s
    positive_count = df["sentiment"].value_counts().get(1, 0)
    
    negative_count = df["sentiment"].value_counts().get(0, 0)
    
    total_comments = positive_count + negative_count
    
    percentage_of_positive_comments = positive_count/total_comments * 100
    # print(f"Percentage of positive comments",percentage_of_positive_comments,"%")
    
    percentage_of_negative_comments = negative_count/total_comments * 100
    # print(f"Percentage of negative comments",percentage_of_negative_comments,"%")
    
    # keys are assigned to each analysis piece so that it is easier to retrieve and display the value in the frontend.
    # So positive_count is the key and count_positive is the value.
    return_back_to_frontend = {
        "df": df,
        "positive_count": int(positive_count),
        "negative_count": int(negative_count),
        "total": int(total_comments),
        "percent_positive": percentage_of_positive_comments,
        "percent_negative": percentage_of_negative_comments,
        # "summary": sentiment_summary(df)
    }   
    
    return return_back_to_frontend          


