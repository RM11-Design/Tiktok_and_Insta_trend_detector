from playwright.sync_api import sync_playwright
import creds
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
    df = pd.read_csv(uploaded_file)
    return df
     
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

# analyzer = SentimentIntensityAnalyzer()

# def get_sentiment(text):
#     scores = analyzer.polarity_scores(text)
#     sentiment = 1 if scores['pos'] > 0 else 0
#     return sentiment

# def overall_sentiment():
#     # print(comments)

#     # Read and find the overall sentiment.

#     df = pd.read_csv('sentiment_for_each_comment.csv')

#     count_positive = df['sentiment'].value_counts().get(1)
#     print(count_positive)

#     count_negative = df['sentiment'].value_counts().get(0)
#     print(count_negative)
    
#     total_comments = count_positive + count_negative
    
#     percentage_of_positive_comments = count_positive/total_comments * 100
#     print(f"Percentage of positive comments",percentage_of_positive_comments,"%")
    
#     percentage_of_negative_comments = count_negative/total_comments * 100
#     print(f"Percentage of negative comments",percentage_of_negative_comments,"%")
    
#     most_common_words = df['Comments'].mode()
    
#     print(f"Most common words found",most_common_words)
            
# overall_sentiment()


