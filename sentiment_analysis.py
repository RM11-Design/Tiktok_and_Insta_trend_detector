from playwright.sync_api import sync_playwright
import csv
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import time

# LINK UPLOAD --------------------------------------------------------------------

# while True:

# instagram_video_link = "https://www.instagram.com/p/DQr0xdwDYnN/?img_index=1"

# def scrape_comments(insta_link):
    
#     comments = []

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False,slow_mo=50)
#         page = browser.new_page()
#         # page.goto(instagram_video_link)
#         page.goto(insta_link)
        
#         # Click on decline cookies    
#         page.get_by_role("button", name="Decline optional cookies").click()
        
#         time.sleep(4)
            
#         # Click on X button   
#         page.locator("div[role='button']", has=page.locator("svg[aria-label='Close']")).click()
        
#         all_spans = page.locator('//span').all()
        
#         time.sleep(3)

#         for span in all_spans:
#             text = span.text_content()
#             if text:
#                 comments.append(text)

#         browser.close()
    
#     return comments

# -------------------------------------------------------------------------------

# This only works when a CSV file is uploaded from the frontend.

def read_comments(uploaded_file):
    # Reads the CSV file that has been uploaded by user
    df = pd.read_csv(uploaded_file)
    # The CSV file is then put into a new CSV called "comments_analysis"
    df.to_csv("comments_analysis.csv", index=False)
    return df 
     
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
    count_positive = df["sentiment"]
    count_positive.value_counts().get(1, 0)
    
    count_negative = df["sentiment"]
    count_negative.value_counts().get(0, 0)
    
    total_comments = count_positive + count_negative
    
    percentage_of_positive_comments = count_positive/total_comments * 100
    # print(f"Percentage of positive comments",percentage_of_positive_comments,"%")
    
    percentage_of_negative_comments = count_negative/total_comments * 100
    # print(f"Percentage of negative comments",percentage_of_negative_comments,"%")
    
    # keys are assigned to each analysis piece so that it is easier to retrieve and display the value in the frontend.
    # So positive_count is the key and count_positive is the value.
    return_back_to_frontend = {
        "df": df,
        "positive_count": count_positive,
        "negative_count": count_negative,
        "total": total_comments,
        "percent_positive": percentage_of_positive_comments,
        "percent_negative": percentage_of_negative_comments
    }   
    
    return return_back_to_frontend          


